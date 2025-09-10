import streamlit as st
from pptx import Presentation
from io import BytesIO

st.title("📊 PowerPoint (.pptx) Uploader")

uploaded_pptx = st.file_uploader("Upload a PowerPoint file", type=["pptx"])

if uploaded_pptx is not None:
    st.success(f"Uploaded: `{uploaded_pptx.name}`")

    # Load presentation
    presentation = Presentation(uploaded_pptx)

    st.write(f"Total slides: {len(presentation.slides)}")

    for i, slide in enumerate(presentation.slides):
        st.header(f"Slide {i + 1}")

        slide_text = ""
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                slide_text += shape.text + "\n"

        if slide_text.strip():
            st.text(slide_text.strip())
        else:
            st.info("No text found on this slide.")
