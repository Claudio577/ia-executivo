import os
from langchain_openai import ChatOpenAI

print(">>> CONFIG.PY CARREGADO")
print(">>> OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
print(">>> MODULO ChatOpenAI =", ChatOpenAI.__module__)

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
