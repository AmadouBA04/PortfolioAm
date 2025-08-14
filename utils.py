import os
import base64
import streamlit as st

def display_image_if_exists(path, caption=None, width=300):
    if os.path.exists(path):
        st.image(path, caption=caption, width=width)
    else:
        st.warning(f"❌ Image introuvable : {path}")

def display_pdf_if_exists(path, height=600):
    if os.path.exists(path):
        with open(path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="{height}px"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.warning(f"❌ PDF introuvable : {path}")