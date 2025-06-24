from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import re


def load_faiss_index(load_path: str = "index/faiss_data") -> FAISS:
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(
        load_path, embedding_model, allow_dangerous_deserialization=True
    )


def get_context_from_query(index, query, k=3):
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
