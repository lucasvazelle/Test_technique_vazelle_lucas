import streamlit as st
import io
import sys
from client_llm import generate
from retriever import load_faiss_index, get_context_from_query
import requests
import json

st.set_page_config(page_title="Chatbot - Powered by Open Source LLM")

st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Ollama & Open Source LLM")

# Initialisation des messages et du contexte
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
if "context" not in st.session_state:
    st.session_state["context"] = []

# Affichage des messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Entrée utilisateur
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response_placeholder = st.chat_message("assistant").empty()

    # Appel de generate avec contexte
    response_stream = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": "modele_llm",
            "prompt": f"""Voici des documents utiles :

{get_context_from_query(load_faiss_index(), prompt)}

En te basant sur ces informations, réponds à la question suivante : 
{prompt}
Réécris l'URL donnée telle quelle dans la source.
""",
            "context": st.session_state["context"],
        },
        stream=True,
    )
    response_stream.raise_for_status()

    full_response = ""
    for line in response_stream.iter_lines():
        body = json.loads(line)
        token = body.get("response", "")
        full_response += token
        response_placeholder.markdown(full_response)

        if "error" in body:
            st.error(f"Erreur : {body['error']}")
            break
        if body.get("done", False):
            st.session_state["context"] = body.get("context", st.session_state["context"])
            break

    st.session_state.messages.append({"role": "assistant", "content": full_response})






#code sans stream

# import streamlit as st
# import io
# import sys
# from client_llm import generate

# st.set_page_config(page_title="Chatbot - Powered by Open Source LLM")

# st.title("💬 Chatbot")
# st.caption("🚀 A streamlit chatbot powered by Ollama & Open Source LLM")

# # Initialisation des messages et du contexte
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
# if "context" not in st.session_state:
#     st.session_state["context"] = []

# # Affichage des messages existants
# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# # Entrée utilisateur
# if prompt := st.chat_input():
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)

#     # Placeholder pour affichage progressif
#     placeholder = st.chat_message("assistant").empty()

#     # Redirection temporaire de stdout vers un buffer texte
#     buffer = io.StringIO()
#     sys_stdout = sys.stdout
#     sys.stdout = buffer

#     try:
#         # Appel direct à ta fonction generate
#         new_context = generate(prompt, st.session_state["context"])
#     finally:
#         # Rétablir stdout même en cas d'erreur
#         sys.stdout = sys_stdout

#     # Récupération du texte imprimé par generate
#     response_text = buffer.getvalue()
#     placeholder.markdown(response_text)
#     st.session_state.messages.append({"role": "assistant", "content": response_text})
#     st.session_state["context"] = new_context


# avec stream propre

# import streamlit as st
# import io
# import sys
# from client_llm import generate

# st.set_page_config(page_title="Chatbot - Powered by Open Source LLM")

# st.title("💬 Chatbot")
# st.caption("🚀 A streamlit chatbot powered by Ollama & Open Source LLM")

# # Initialisation des messages et du contexte
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
# if "context" not in st.session_state:
#     st.session_state["context"] = []

# # Affichage des messages existants
# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# # Entrée utilisateur
# if prompt := st.chat_input():
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)

#     response_box = st.chat_message("assistant").empty()
#     full_response = ""
#     new_context = st.session_state["context"]

#     # Appel de generate comme générateur
#     generator = generate(prompt, st.session_state["context"])
#     for chunk in generator:
#         if isinstance(chunk, dict) and "context" in chunk:
#             new_context = chunk["context"]
#         else:
#             full_response += chunk
#             response_box.markdown(full_response)

#     st.session_state.messages.append({"role": "assistant", "content": full_response})
#     st.session_state["context"] = new_context
