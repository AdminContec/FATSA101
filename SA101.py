import streamlit as st
import pandas as pd
import plotly.express as px

# Título do app
st.title("Dashboard Interativo - Dados de matr020_100425")

# Carregar dados
df = pd.read_csv("matr020_100425.csv")

st.subheader("Prévia dos dados")
st.dataframe(df)

# Filtros interativos
st.sidebar.header("Filtros")
coluna_filtro = st.sidebar.selectbox("Escolha uma coluna para filtrar:", df.columns)
valores_unicos = df[coluna_filtro].dropna().unique()
valores_filtrados = st.sidebar.multiselect("Valores:", valores_unicos, default=valores_unicos)

# Aplicar filtro
df_filtrado = df[df[coluna_filtro].isin(valores_filtrados)]

st.subheader("Tabela Dinâmica com Filtro")
st.dataframe(df_filtrado)

# Gráfico
st.subheader("Gráfico")
coluna_x = st.selectbox("Eixo X:", df.columns)
coluna_y = st.selectbox("Eixo Y:", df.columns)

fig = px.bar(df_filtrado, x=coluna_x, y=coluna_y)
st.plotly_chart(fig)
