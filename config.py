import os
from langchain_openai.chat_models import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")
    )
