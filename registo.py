import streamlit as st
import pandas as pd
from datetime import datetime
import os

FICHEIRO_DADOS = "ocorrencias.csv"
tecnicos = ["Bruno Guerreiro", "Ronaldo Tavares", "Pedro Puga", "José Reis"]

st.set_page_config(page_title="Registo de Ocorrências", layout="centered")

# Inicializar sessão
if "tecnico_selecionado" not in st.session_state:
    st.session_state.tecnico_selecionado = None
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "selecionar"

# Página 1: Seleção do técnico
if st.session_state.pagina_atual == "selecionar":
    st.markdown("""
        <div style='text-align: center;'>
            DPD logo.jpg
            <h1>📘 Registo de Ocorrências Noturnas</h1>
        </div>
    """, unsafe_allow_html=True)

    tecnico = st.selectbox("Escolha o seu nome:", tecnicos)
    if st.button("Continuar"):
        st.session_state.tecnico_selecionado = tecnico
        st.session_state.pagina_atual = "registo"

# Página 2: Registo de ocorrência
elif st.session_state.pagina_atual == "registo":
    st.title("📋 Registo de Ocorrência")
    st.markdown(f"**Técnico:** {st.session_state.tecnico_selecionado}")

    with st.form("form_ocorrencia"):
        data = st.date_input("Data", value=datetime.today())
        localizacao = st.text_input("Localização")
        ocorrencia = st.text_area("Descrição da Ocorrência")
        acao = st.text_area("Ação Tomada")
        submeter = st.form_submit_button("Submeter")

        if submeter:
            nova_ocorrencia = {
                "Data": data.strftime("%Y-%m-%d"),
                "Técnico": st.session_state.tecnico_selecionado,
                "Localização": localizacao,
                "Ocorrência": ocorrencia,
                "Ação Tomada": acao
            }

            if os.path.exists(FICHEIRO_DADOS):
                df = pd.read_csv(FICHEIRO_DADOS)
                df = pd.concat([df, pd.DataFrame([nova_ocorrencia])], ignore_index=True)
            else:
                df = pd.DataFrame([nova_ocorrencia])

            df.to_csv(FICHEIRO_DADOS, index=False)
            st.success("✅ Ocorrência registada com sucesso!")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Ver Ocorrências"):
            st.session_state.pagina_atual = "visualizar"
    with col2:
        if st.button("🚪 Sair"):
            st.session_state.tecnico_selecionado = None
            st.session_state.pagina_atual = "selecionar"

# Página 3: Visualização das ocorrências
elif st.session_state.pagina_atual == "visualizar":
    st.title("📊 Ocorrências Registadas")
    if os.path.exists(FICHEIRO_DADOS):
        df = pd.read_csv(FICHEIRO_DADOS)
        st.dataframe(df)
    else:
        st.info("Ainda não existem ocorrências registadas.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Voltar ao Registo"):
            st.session_state.pagina_atual = "registo"
    with col2:
        if st.button("🚪 Sair"):
            st.session_state.tecnico_selecionado = None
            st.session_state.pagina_atual = "selecionar"
