# streamlit_app.py
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from run_rag import answer_question_with_rag

st.set_page_config(page_title="RAG Research Assistant", layout="centered")

st.title("🔍 Research Assistant using RAG")
st.markdown("Ask a research question, and get a concise answer from the latest arXiv papers.")

# Input
question = st.text_input("Enter your research question:")

if st.button("Generate Answer"):
    if not question.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Retrieving documents and generating response..."):
            response = answer_question_with_rag(question)
            st.markdown("### 📌 Answer")
            st.write(response)
