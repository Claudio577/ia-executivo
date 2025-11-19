import os
import streamlit as st
from langchain_openai import ChatOpenAI

st.write(">>> CONFIG.PY CARREGADO")
st.write(">>> OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
st.write(">>> ChatOpenAI vindo de:", ChatOpenAI.__module__)
st.write(">>> Executando get_llm()")

def get_llm():
    key = os.getenv("OPENAI_API_KEY")
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        openai_api_key=key
    )
