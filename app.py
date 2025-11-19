import streamlit as st
from agents.agente_executivo import criar_agente_executivo

st.title("💼 Agente Executivo – Estratégia Corporativa")

query = st.text_area("Digite sua pergunta:")

if st.button("Enviar"):
    agente = criar_agente_executivo()
    resposta = agente.invoke({"input": query})

    st.subheader("📌 Resposta Executiva")
    st.write(resposta["text"])
