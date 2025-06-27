import streamlit as st
from utils.styles import inject_navigation_css

# Page principale de l'application

st.image("https://basegun.interieur.gouv.fr/assets/logo_dtnum-BjUxmtCL.jpg", width=300)

st.set_page_config(page_title="Assistant DGFiP", page_icon="📄", layout="wide")
inject_navigation_css()

st.markdown("# Bienvenue")
st.markdown("Cette application contient un mini chat bot DGFIP.")
st.markdown(
    "Cette application à été produite par Vazelle Lucas dans le cadre d'un test technique."
)
st.markdown("Utilisez la barre latérale pour explorer l'application.")

if st.button("Tester le chat bot"):
    st.switch_page(
        "pages/1 Assistant.py"
    )  

if st.button("Voir mon CV"):
    st.switch_page("pages/2 CV.py")  

if st.button("Voir les consignes du test"):
    st.switch_page(
        "pages/3 Consignes.py"
    )  