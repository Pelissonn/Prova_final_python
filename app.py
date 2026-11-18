import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Prova 3B1", layout="wide")

#tratamento da tabela
tab_prova = pd.read_csv("bd_iqvu_1994_2016.csv", sep=";", decimal=",", encoding="latin-1")

tab_prova = tab_prova.rename(columns={"ï»¿SERIE": "SERIE"})

df_filtrado = tab_prova[
    (tab_prova["NOMEUP"].isin(["Taquaril", "Santa Ines"])) & (tab_prova["SERIE"] == "SERIE HISTORICA")
 ].copy()
df_tabela = df_filtrado[["NOMEUP", "ANO", "IQVU"]]

#dataframe 
try:
 # 3. barra lateral e titulo

 st.title("Painel Streamlit do IQVU de Belo Horizonte — Taquaril e Santa Inês")

 #sidebar
 st.sidebar.header("Controles")
 opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

 if opcao == "Tabela":
    st.header("Tabela do IQVU (Série Histórica)")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

 elif opcao == "Gráficos":
    st.header("Gráficos do IQVU — Taquaril e Santa Inês")

    # --------------------------------------------------------------------------
    # GRÁFICO 1: Linha Individual - Taquaril (Exigido na Prova)
    # --------------------------------------------------------------------------
    st.subheader("1. Gráfico de Linha — Taquaril")
    df_taquaril = df_tabela[df_tabela["NOMEUP"] == "Taquaril"]

    fig_linha_taquaril = px.line(
        df_taquaril,
        x="ANO",
        y="IQVU",
        markers=True,
        title="Evolução do IQVU — Taquaril (1994 a 2016)",
        template="plotly_dark"
    )
    fig_linha_taquaril.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
    fig_linha_taquaril.update_xaxes(type="category")
    fig_linha_taquaril.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_linha_taquaril, use_container_width=True)

    # --------------------------------------------------------------------------
    # GRÁFICO 2: Linha Individual - Santa Inês (Exigido na Prova)
    # --------------------------------------------------------------------------
    st.subheader("2. Gráfico de Linha — Santa Inês")
    df_santa_ines = df_tabela[df_tabela["NOMEUP"] == "Santa Ines"]

    fig_linha_santa_ines = px.line(
        df_santa_ines,
        x="ANO",
        y="IQVU",
        markers=True,
        title="Evolução do IQVU — Santa Inês (1994 a 2016)",
        template="plotly_dark"
    )
    fig_linha_santa_ines.update_traces(line_color="#00F5D4", line_width=3, marker_size=8)
    fig_linha_santa_ines.update_xaxes(type="category")
    fig_linha_santa_ines.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_linha_santa_ines, use_container_width=True)


 # 5. FONTE DOS DADOS (Obrigatória no painel)
 st.markdown("---")
 st.caption("Fonte dos dados: dados abertos da Prefeitura de Belo Horizonte — https://dados.pbh.gov.br/")

except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
    st.info("Certifique-se de que o arquivo 'tabela 1.1.2.xls está no mesmo diretório do script")