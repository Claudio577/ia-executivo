import os
from langchain_openai import ChatOpenAI

print(">>> CONFIG.PY CARREGADO")
print(">>> OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
print(">>> ChatOpenAI vindo de:", ChatOpenAI.__module__)
print(">>> Executando get_llm()")

def get_llm():
    key = os.getenv("OPENAI_API_KEY")
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        openai_api_key=key
    )
