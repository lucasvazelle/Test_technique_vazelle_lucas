import requests
import json
from langchain.schema import Document
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from pprint import pprint
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
import os

model = "modele_llm"
load_path = "../notebooks/faiss_data"  


def load_faiss_index(load_path: str = "../notebooks/faiss_data"  ) -> FAISS:
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(
        load_path, 
        embedding_model, 
        allow_dangerous_deserialization=True  # à activer uniquement pour des documents vérifiées
    )

# Récupère les k documents pertinents et les assemble en contexte brut
def get_context_from_query(index, query, k=3):
    docs = index.similarity_search(query, k=k)

    context_parts = []
    for doc in docs:
        titre = doc.metadata.get("titre", "Titre inconnu")
        source = doc.metadata.get("source", "Source inconnue")
        contenu = doc.page_content

        formatted_doc = f"TITRE : {titre}\nSOURCE : {source}\n\n{contenu}"
        context_parts.append(formatted_doc)

    context_text = "\n\n---\n\n".join(context_parts)
    return context_text



# Génère une réponse en utilisant l’API du LLM local + le contexte FAISS
def generate(user_input, previous_context):
    index = load_faiss_index()
    retrieved_context = get_context_from_query(index, user_input)

    prompt = f"""Voici des documents utiles : 

{retrieved_context}

En te basant sur ces informations, réponds à la question suivante : 
{user_input}
"""

    r = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "context": previous_context,
        },
        stream=True,
    )
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get("response", "")
        print(response_part, end="", flush=True)

        if "error" in body:
            raise Exception(body["error"])

        if body.get("done", False):
            return body["context"]

def main():
    context = []
    while True:
        user_input = input("Posez votre question \n\n")
        print()  # espace
        context = generate(
            user_input, context
        )  # context est auto-alimenté par les query précedentes


if __name__ == "__main__":
    main()
