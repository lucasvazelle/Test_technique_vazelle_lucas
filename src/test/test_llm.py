import requests
import json

model = "model_llama_1b"


def generate(user_input, context):
    r = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": model,
            "prompt": user_input,
            "context": context,
        },
        stream=True,  # voir réponse en temps réel
    )
    r.raise_for_status()  # recevoir les erreurs

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get("response", "")
        print(response_part, end="", flush=True)  # vide memoire tampon

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