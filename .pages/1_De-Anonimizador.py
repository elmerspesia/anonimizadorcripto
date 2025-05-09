import streamlit as st
import pandas as pd
from io import BytesIO
import utils

st.set_page_config(page_title="De-Anonimizador", layout="wide")

st.sidebar.title("Menu")
st.sidebar.markdown("## De-Anonimizador")

st.title("🔓 De-Anonimizador de Dados")

uploaded_file = st.file_uploader("Selecione o arquivo anonimizado", type=["csv", "xlsx", "txt"])

if uploaded_file:
    ext = uploaded_file.name.split(".")[-1].lower()
    if ext == "csv":
        df = pd.read_csv(uploaded_file)
    elif ext == "xlsx":
        df = pd.read_excel(uploaded_file)
    elif ext == "txt":
        df = pd.read_csv(uploaded_file, sep="\t")
    else:
        st.error("Formato não suportado.")
        st.stop()

    st.subheader("Pré-visualização dos dados anonimados")
    st.dataframe(df)

    if st.button("Desanonimizar"):
        with st.spinner("Desanonimizando dados..."):
            try:
                recovered_df = utils.deanonymize_data(df)
                st.success("Desanonimização concluída.")
                st.dataframe(recovered_df)

                buffer = BytesIO()
                export_format = st.selectbox("Formato para download", ["CSV", "XLSX", "TXT"])
                file_name = st.text_input("Nome do arquivo de saída", value="dados_original")

                utils.export_dataframe(recovered_df, buffer, export_format)
                st.download_button("📥 Baixar arquivo original", buffer.getvalue(), f"{file_name}.{export_format.lower()}")

            except Exception as e:
                st.error(f"Erro ao desanonimizar: {e}")
