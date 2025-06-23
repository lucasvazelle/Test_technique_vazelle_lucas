import base64
import streamlit as st

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    ext = image_path.split('.')[-1].lower()
    mime = "jpeg" if ext in ["jpg", "jpeg"] else ext
    return f"data:image/{mime};base64,{encoded}"

def inject_navigation_css():
    st.markdown("""
        <style>
        header, footer, [data-testid="stSidebarCollapse"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
