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
