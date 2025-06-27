import streamlit as st
from utils.styles import get_base64_image

st.set_page_config(page_title="Mon CV", page_icon="📄", layout="wide")

if st.button("⬅ Quitter le CV"):
    st.switch_page(
        "pages/1 Assistant.py"
    ) 
bg_img = get_base64_image("media/CV.jpg")

# CSS pour affichage plein écran + suppression header/footer/sidebar
st.markdown(
    f"""
    <style>
    header, footer, [data-testid="stSidebar"], button[title="Open sidebar"], button[title="Close sidebar"] {{
        display: none !important;
    }}

    .main .block-container {{
        padding: 0 !important;
        margin: 0 !important;
    }}

    .section-cv {{
        height: 75vh;
        width: 75vw;
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
""",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="section-cv">
        <div class="exit-btn">
""",
    unsafe_allow_html=True,
)


st.markdown("</div></div>", unsafe_allow_html=True)
