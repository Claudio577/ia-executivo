from langchain.chat_models import init_chat_model
import os

print(">>> CONFIG.PY CARREGADO")
print(">>> OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
print(">>> MODULO ChatOpenAI =", ChatOpenAI.__module__)

def get_llm():
    return init_chat_model(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.1,
    )
