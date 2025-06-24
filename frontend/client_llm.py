import requests
import json
from retriever import load_faiss_index, get_context_from_query
import os

model = "model_llama_3b"


def get_ollama_url():
    # Récupère le mode d'exécution ('local' ou 'docker'), défaut à 'local'
    mode = os.getenv("APP_ENV", "local")
    if mode == "docker":
        return "http://ollama:11434/api/generate"
    else:
        return "http://127.0.0.1:11434/api/generate"
    

def generate(user_input, previous_context):
    index = load_faiss_index()
    retrieved_context = get_context_from_query(index, user_input)

    prompt = f"""Voici des documents utiles : \n\n

            {retrieved_context}\n\n

            En te basant sur ces fiches, re donne la fiche qui réponds à la question suivante, met en avant l'élément de la fiche qui permet de répondre à la question : 
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
        print(body.get("response", ""), end="", flush=True)
        if "error" in body:
            raise Exception(body["error"])
        if body.get("done", False):
            return body["context"]



def generate_to_streamlit(user_input, previous_context):
    index = load_faiss_index()
    retrieved_context = get_context_from_query(index, user_input)

    url = get_ollama_url()

    prompt = f""""Voici des fiches utiles : \n\n

            {retrieved_context}\n\n

            Voici la question de l'utilisateur  {user_input}. N'invente rien s'il te plaît.
            """

    r = requests.post(
        url,
        json={
            "model": model,
            "prompt": prompt,
            "context": previous_context,
        },
        stream=True,
    )
    r.raise_for_status()

    return r




    