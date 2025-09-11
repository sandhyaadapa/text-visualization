# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSV Analyzer", layout="wide")

st.title("📊 CSV Data Analyzer")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    
    # Show data
    st.subheader("Data Preview")
    st.dataframe(df)

    # Show basic statistics
    st.subheader("Descriptive Statistics")
    st.write(df.describe())

    # Column selection for plotting
    st.subheader("📈 Plot a Column")
    column_to_plot = st.selectbox("Select numeric column to plot", df.select_dtypes(include='number').columns)

    if column_to_plot:
        fig, ax = plt.subplots()
        df[column_to_plot].plot(kind='hist', ax=ax, bins=20, color='skyblue')
        ax.set_title(f'Distribution of {column_to_plot}')
        st.pyplot(fig)
else:
    st.info("👈 Upload a CSV file to get started.")
