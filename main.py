import streamlit as st
from PIL import Image

logo = Image.open("spesia_logo.png")
st.set_page_config(page_title="Spesia - Anonimizador de Dados", page_icon=logo)

col1, col2 = st.columns([1, 4])
with col1:
    st.image(logo, width=80)
with col2:
    st.markdown("<h1 style='margin-top: 10px;'>Spesia - Anonimizador de Dados</h1>", unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("### Login de Acesso")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if username == "spesia123" and password == "spesia123":
            st.success("Login bem-sucedido!")
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
else:
    st.markdown("✅ Use o menu lateral para acessar as funcionalidades.")
