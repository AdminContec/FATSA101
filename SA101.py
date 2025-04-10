import streamlit as st
import pandas as pd
import plotly.express as px

# Título do app
st.title("Dashboard de Matrículas")

# Carregando os dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("matr020_100425.csv", sep=';', encoding='latin1')

df = carregar_dados()

# Exibe a tabela original
st.subheader("Tabela de Dados")
st.dataframe(df)

# Criação de Tabela Dinâmica
st.subheader("Tabela Dinâmica")

# Seleção de colunas para index, columns e values
colunas = df.columns.tolist()
indice = st.selectbox("Selecione o índice (linhas)", colunas, index=0)
coluna = st.selectbox("Selecione a coluna (colunas)", colunas, index=1)
valor = st.selectbox("Selecione o valor", colunas, index=2)

# Criação da pivot table
try:
    tabela_dinamica = pd.pivot_table(df, index=indice, columns=coluna, values=valor, aggfunc='sum', fill_value=0)
    st.dataframe(tabela_dinamica)
except Exception as e:
    st.warning(f"Erro ao criar tabela dinâmica: {e}")

# Gráfico
st.subheader("Gráfico de Barras")

# Seleciona coluna para agrupar
coluna_grafico = st.selectbox("Selecione uma coluna para agrupar no gráfico", colunas)

# Agrupamento e plot
try:
    dados_grafico = df[coluna_grafico].value_counts().reset_index()
    dados_grafico.columns = [coluna_grafico, 'Contagem']
    fig = px.bar(dados_grafico, x=coluna_grafico, y='Contagem', title=f"Distribuição de {coluna_grafico}")
    st.plotly_chart(fig)
except Exception as e:
    st.warning(f"Erro ao gerar gráfico: {e}")
