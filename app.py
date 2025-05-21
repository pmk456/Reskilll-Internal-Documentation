import streamlit as st
import os

st.set_page_config("Internal Documentation Dashboard", layout="wide")
st.title("Internal Documentation Portal")

# Map of sections and their folder names
doc_sections = {
    "Frontend": "frontend",
    "Backend": "backend",
    "Authentication": "authentication",
    "DevOps": "devops",
    "Database": "database",
    "Common": "common"
}

# Sidebar layout
st.sidebar.header("Select Documentation Area")
section = st.sidebar.selectbox("Choose Category", list(doc_sections.keys()))
folder_path = os.path.join("docs", doc_sections[section])

md_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
file_choice = st.sidebar.radio("Choose Document", md_files)

md_path = os.path.join(folder_path, file_choice)
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

st.markdown(f"### `{file_choice}`")
st.markdown(md_content, unsafe_allow_html=True)
