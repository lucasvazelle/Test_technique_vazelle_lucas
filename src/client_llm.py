import requests
import json
from retriever import load_faiss_index, get_context_from_query

model = "modele_llm"

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
        print(body.get("response", ""), end="", flush=True)
        if "error" in body:
            raise Exception(body["error"])
        if body.get("done", False):
            return body["context"]


def generate_to_streamlit(user_input, previous_context):
    index = load_faiss_index()
    retrieved_context = get_context_from_query(index, user_input)

    prompt = f"""Voici des documents utiles : 

{retrieved_context}

En te basant sur ces informations, réponds à la question suivante : 
{user_input}
Réécris l'URL donnée telle quelle dans la source.
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

    context_final = previous_context

    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
        if "response" in body:
            yield body["response"]  # <- on stream le token
        if body.get("done", False):
            context_final = body.get("context", previous_context)
            break

    yield {"context": context_final}  # signal de fin avec contexte
