# app.py
import streamlit as st
import json
from client_llm import generate_to_streamlit

# Configuration
st.set_page_config(
    page_title="Assistant DGFiP",
    page_icon="📄",
    layout="centered"
)

# HEADER DGFiP
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fb;
    }
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .user-msg {
        background-color: #white;
    }
    .assistant-msg {
        background-color: #white;
    }
    </style>
""", unsafe_allow_html=True)

st.image("https://basegun.interieur.gouv.fr/assets/logo_dtnum-BjUxmtCL.jpg", width=120)
st.title("Assistant interne - DGFiP")
st.subheader("Vazelle Lucas - test technique")
st.caption("Obtenez une fiche pratique adaptée à votre question")

# Initialisation de session
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Bonjour ! Posez-moi une question"}
    ]
if "context" not in st.session_state:
    st.session_state["context"] = []

# Affichage historique messages
for msg in st.session_state.messages:
    role_class = "user-msg" if msg["role"] == "user" else "assistant-msg"
    st.chat_message(msg["role"]).markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# Saisie utilisateur
if prompt := st.chat_input("Posez votre question (ex. : Comment déclarer un revenu foncier ?)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(f"<div class='user-msg'>{prompt}</div>", unsafe_allow_html=True)

    placeholder = st.chat_message("assistant").empty()

    try:
        response_stream = generate_to_streamlit(prompt, st.session_state["context"]) 
        full_response = ""
        for line in response_stream.iter_lines():
            body = json.loads(line)
            token = body.get("response", "")
            full_response += token
            placeholder.markdown(f"<div class='assistant-msg'>{full_response}</div>", unsafe_allow_html=True)

            if "error" in body:
                st.error(f"Erreur : {body['error']}")
                break
            if body.get("done", False):
                st.session_state["context"] = body.get("context", st.session_state["context"])
                break

        st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"Erreur de génération : {str(e)}")

# Footer


