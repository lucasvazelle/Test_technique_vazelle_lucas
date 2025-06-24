from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import re

# import spacy


def nettoyer_prompt(prompt: str) -> str:
    # nlp = spacy.load("fr_core_news_sm")
    # suppression d'expressions parasites
    expressions_parasites = [
        r"je voudrais savoir",
        r"peux[- ]tu me dire",
        r"est[- ]ce que tu peux me dire",
        r"je cherche à savoir",
        r"pourrais[- ]tu me dire",
        r"est[- ]ce que",
        r"dis[- ]moi",
        r"saurais[- ]tu",
        r"j'aimerais savoir",
        r"est[- ]ce qu’on peut",
        r"merci de me dire",
        r"du coup",
        r"en fait",
        r"\b(euh|alors|donc|bah|ben|hein|quoi|voilà|genre)\b",
    ]
    pattern = re.compile("|".join(expressions_parasites), flags=re.IGNORECASE)
    cleaned = pattern.sub("", prompt)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    # traitement NLP avec spaCy
    doc = nlp(cleaned)

    #  lemmatisation + suppression des stop words et de la ponctuation
    mots_utiles = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct and token.lemma_ != ""
    ]

    # Reconstruction de la phrase
    return " ".join(mots_utiles)


def load_faiss_index(load_path: str = "../index/faiss_data") -> FAISS:
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(
        load_path, embedding_model, allow_dangerous_deserialization=True
    )


def get_context_from_query(index, query, k=3):
    # query_nettoye = nettoyer_prompt(query)
    # docs = index.similarity_search(query_nettoye, k=k)
    docs = index.similarity_search(query, k=k)
    sources = []

    context_parts = []
    for doc in docs:
        titre = doc.metadata.get("titre", "Titre inconnu")
        source = doc.metadata.get("source", "Source inconnue")
        contenu = doc.page_content
        formatted_doc = f"FICHE : TITRE : {titre}\n\n{contenu}\n\nSOURCE URL à donner à l'utilisateur : {source}"
        context_parts.append(formatted_doc)
        sources.append(source)

    context_text = "\n\n---\n\n".join(context_parts)
    return context_text
