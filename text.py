import streamlit as st
from PyPDF2 import PdfReader

st.title("📄 PDF Uploader")

# Upload PDF file
uploaded_file = st.file_uploader("Drag and drop a PDF file here", type="pdf")

if uploaded_file is not None:
    # Read PDF using PyPDF2
    reader = PdfReader(uploaded_file)
    num_pages = len(reader.pages)
    st.success(f"Uploaded: `{uploaded_file.name}` with **{num_pages} pages**")

    # Display content of first few pages
    for i in range(min(3, num_pages)):
        text = reader.pages[i].extract_text()
        st.subheader(f"Page {i+1}")
        st.text(text if text else "[No text extracted from this page]")
