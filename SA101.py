import streamlit as st
import pandas as pd

# Configuração inicial da página
st.set_page_config(
    page_title="Análise de Dados",
    page_icon="📊",
    layout="wide"
)

# Título do aplicativo
st.title("📊 Análise de Dados CSV")

# Upload do arquivo
uploaded_file = st.file_uploader("Carregue seu arquivo CSV", type=["csv"])

if uploaded_file is not None:
    try:
        # Lendo o arquivo CSV
        df = pd.read_csv(uploaded_file)
        
        # Mostrando informações básicas
        st.success("Arquivo carregado com sucesso!")
        
        # Abas
        tab1, tab2, tab3 = st.tabs(["Dados", "Estatísticas", "Visualização"])
        
        with tab1:
            st.subheader("Visualização dos Dados")
            st.dataframe(df)
            
        with tab2:
            st.subheader("Estatísticas Descritivas")
            st.write(df.describe())
            
        with tab3:
            st.subheader("Visualização Gráfica")
            column = st.selectbox("Selecione uma coluna para visualizar", df.columns)
            
            if pd.api.types.is_numeric_dtype(df[column]):
                st.bar_chart(df[column])
            else:
                st.write("Selecione uma coluna numérica para visualização gráfica.")
                
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
else:
    st.info("Por favor, carregue um arquivo CSV para começar.")
