import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

# Load sample data
df = sns.load_dataset('iris')

# Page title
st.title("📊 Three Visualizations in One Streamlit App")

# --- 1. Matplotlib Scatter Plot ---
st.header("1. Matplotlib: Sepal Length vs Sepal Width")
fig1, ax1 = plt.subplots()
species = df['species'].unique()
colors = ['red', 'green', 'blue']

for sp, color in zip(species, colors):
    subset = df[df['species'] == sp]
    ax1.scatter(subset['sepal_length'], subset['sepal_width'], label=sp, color=color)

ax1.set_xlabel("Sepal Length")
ax1.set_ylabel("Sepal Width")
ax1.legend()
st.pyplot(fig1)

# --- 2. Seaborn Boxplot ---
st.header("2. Seaborn: Petal Length Distribution by Species")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='species', y='petal_length', ax=ax2, palette="pastel")
st.pyplot(fig2)

# --- 3. Plotly Bar Chart ---
st.header("3. Plotly: Average Petal Width by Species")
avg_petal_width = df.groupby("species")["petal_width"].mean().reset_index()
fig3 = px.bar(avg_petal_width, x="species", y="petal_width",
              labels={"petal_width": "Average Petal Width"},
              color="species",
              title="Average Petal Width by Species")
st.plotly_chart(fig3)

