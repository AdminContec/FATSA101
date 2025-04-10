import streamlit as st
import pandas as pd
import plotly.express as px

# Título do app
st.title("Dashboard de Matrículas com Upload de Arquivo")

# Upload de Arquivo
st.subheader("Carregar Arquivo CSV")
arquivo = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if arquivo is not None:
    try:
        df = pd.read_csv(arquivo, sep=';', encoding='latin1')

        # Exibe a tabela original
        st.subheader("Tabela de Dados")
        st.dataframe(df)

        # Tabela Dinâmica
        st.subheader("Tabela Dinâmica")
        colunas = df.columns.tolist()

        if len(colunas) >= 3:
            indice = st.selectbox("Selecione o índice (linhas)", colunas, index=0)
            coluna = st.selectbox("Selecione a coluna (colunas)", colunas, index=1)
            valor = st.selectbox("Selecione o valor", colunas, index=2)

            try:
                tabela_dinamica = pd.pivot_table(df, index=indice, columns=coluna, values=valor, aggfunc='sum', fill_value=0)
                st.dataframe(tabela_dinamica)
            except Exception as e:
                st.warning(f"Erro ao criar tabela dinâmica: {e}")
        else:
            st.warning("O arquivo precisa ter pelo menos 3 colunas para a tabela dinâmica.")

        # Gráfico
        st.subheader("Gráfico de Barras")
        coluna_grafico = st.selectbox("Selecione uma coluna para agrupar no gráfico", df.columns)

        try:
            dados_grafico = df[coluna_grafico].value_counts().reset_index()
            dados_grafico.columns = [coluna_grafico, 'Contagem']
            fig = px.bar(dados_grafico, x=coluna_grafico, y='Contagem', title=f"Distribuição de {coluna_grafico}")
            st.plotly_chart(fig)
        except Exception as e:
            st.warning(f"Erro ao gerar gráfico: {e}")

    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
else:
    st.info("Por favor, carregue um arquivo CSV para começar.")
