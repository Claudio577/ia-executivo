from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from config import get_llm

EXECUTIVE_PROMPT = """
Você é um Executivo Sênior especializado em estratégia corporativa.
Responda sempre de maneira clara, objetiva e estruturada.
"""

def criar_agente_executivo():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", EXECUTIVE_PROMPT),
        ("human", "{input}")
    ])

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain
