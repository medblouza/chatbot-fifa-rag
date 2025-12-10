import streamlit as st
import requests

st.title("Chatbot FIFA RAG")

query = st.text_input("Pose une question")

if st.button("Envoyer"):
    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"query": query}
    )
    st.write(response.json()["answer"])
