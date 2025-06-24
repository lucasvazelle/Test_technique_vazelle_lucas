import streamlit as st
import json
import sys
import os
from client_llm import generate_to_streamlit

st.set_page_config(page_title="Assistant DGFiP", page_icon="")
st.image("https://basegun.interieur.gouv.fr/assets/logo_dtnum-BjUxmtCL.jpg", width=150)

st.title("Assistant - DGFiP")
st.caption("Obtenez une fiche pratique adaptée à votre question.")

# Session init
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Bonjour ! Posez-moi une question"}]
if "context" not in st.session_state:
    st.session_state["context"] = []

# Affichage historique
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Posez votre question (ex. : Quels droits réels immobiliers peuvent être donnés par acte notarié ?)"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    placeholder = st.chat_message("assistant").empty()

    try:
        stream = generate_to_streamlit(prompt, st.session_state["context"])
        full_response = ""
        for line in stream.iter_lines():
            try:
                data = json.loads(line)
                token = data.get("response", "")
                full_response += token
                placeholder.markdown(full_response)

                if "error" in data:
                    st.error(f"Erreur LLM : {data['error']}")
                    break
                if data.get("done"):
                    st.session_state["context"] = data.get("context", [])
                    break
            except json.JSONDecodeError:
                continue

        st.session_state["messages"].append({"role": "assistant", "content": full_response})
    except Exception as e:
        st.error(f"Erreur technique : {e}")

