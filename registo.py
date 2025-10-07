# Página 1: Seleção do técnico
if st.session_state.pagina_atual == "selecionar":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("DPD logo.jpg", width=200)
        st.markdown("<h1 style='text-align: center;'>📘 Registo de Ocorrências Noturnas</h1>", unsafe_allow_html=True)

    tecnico = st.selectbox("Escolha o seu nome:", tecnicos)
    if st.button("Continuar"):
        st.session_state.tecnico_selecionado = tecnico
        st.session_state.pagina_atual = "registo"
