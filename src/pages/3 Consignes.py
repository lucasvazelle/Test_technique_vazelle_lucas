import streamlit as st
from utils.styles import get_base64_image

# Configuration de la page
st.set_page_config(page_title="Mon CV", page_icon="📄", layout="wide")


# Bouton "Quitter le CV"
if st.button("⬅ Quitter les consignes"):
    st.switch_page("pages/1 Assistant.py")  # Change le chemin selon ta page d'accueil réelle

# Image de fond (ton CV)
bg_img = get_base64_image("media/test.jpg")

# CSS pour affichage plein écran + suppression header/footer/sidebar
st.markdown(f"""
    <style>
    header, footer, [data-testid="stSidebar"], button[title="Open sidebar"], button[title="Close sidebar"] {{
        display: none !important;
    }}

    .main .block-container {{
        padding: 0 !important;
        margin: 0 !important;
    }}

    .section-cv {{
        height: 80vh;
        width: 80vw;
        background-image: url("{bg_img}");
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
        background-color: white;
        position: relative;
    }}

    .exit-btn {{
        position: absolute;
        top: 10px;
        left: 10px;
        z-index: 100;
    }}
    </style>
""", unsafe_allow_html=True)

# Contenu HTML avec bouton
st.markdown(f"""
    <div class="section-cv">
        <div class="exit-btn">
""", unsafe_allow_html=True)


st.markdown("</div></div>", unsafe_allow_html=True)
    