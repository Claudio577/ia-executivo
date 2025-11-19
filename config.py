import os

# IMPORTAÇÃO OBRIGATÓRIA — evita conflito
from langchain_openai.chat_models import ChatOpenAI

print(">>> ChatOpenAI carregado de:", ChatOpenAI.__module__)

def get_llm():
    print(">>> Executando get_llm()")
    key = os.getenv("OPENAI_API_KEY")
    print(">>> OPENAI_API_KEY =", key)

    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        api_key=key
    )
