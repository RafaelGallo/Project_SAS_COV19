import os
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.signal import find_peaks

# ==============================================================
# 1. Configuração inicial
# ==============================================================

st.set_page_config(
    page_title="Painel COVID-19 Brasil",
    page_icon="🦠",
    layout="wide"
)

st.title("📊 Painel Epidemiológico COVID-19 — Brasil (2020 – 2025)")
st.markdown(
    "Visualização interativa dos principais indicadores epidemiológicos "
    "baseados em dados oficiais do Ministério da Saúde (OpenDataSUS)."
)

# ==============================================================
# 2. Carregamento do dataset consolidado
# ==============================================================

@st.cache_data
def load_data():
    csv_path = (
        r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\covid19_SP"
        r"\SaS_Cov19_project\output\COVIDBR\COVIDBR_2020_2025_Consolidado.csv"
    )
    df = pd.read_csv(csv_path, sep=";", encoding="utf-8", low_memory=False)
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df = df[(df["casosNovos"] >= 0) & (df["obitosNovos"] >= 0)]
    return df

df = load_data()

# ==============================================================
# 3. Estrutura de abas
# ==============================================================

tabs = st.tabs([
    "📈 Evolução Nacional",
    "🏙️ Município de São Paulo",
    "🗺️ Regiões do Brasil",
    "📊 Top Municípios e Estados",
    "⚰️ Taxa de Mortalidade"
])

# ==============================================================
# 4. Aba 1 – Evolução Nacional
# ==============================================================

with tabs[0]:
    st.subheader("Evolução da COVID-19 no Brasil — Casos × Óbitos (MM 7 dias)")

    df_brasil = (
        df.groupby("data")[["casosNovos", "obitosNovos"]]
        .sum()
        .reset_index()
        .sort_values("data")
    )
    df_brasil["casosMM7"] = df_brasil["casosNovos"].rolling(7, min_periods=1).mean()
    df_brasil["obitosMM7"] = df_brasil["obitosNovos"].rolling(7, min_periods=1).mean()

    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df_brasil["data"], df_brasil["casosMM7"], color="tab:blue", linewidth=2)
    ax1.fill_between(df_brasil["data"], df_brasil["casosMM7"], color="skyblue", alpha=0.3)
    ax1.set_ylabel("Casos diários (MM 7 dias)", color="tab:blue")
    ax1.tick_params(axis="y", labelcolor="tab:blue")
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    ax2 = ax1.twinx()
    ax2.plot(df_brasil["data"], df_brasil["obitosMM7"], color="tab:orange", linewidth=2)
    ax2.fill_between(df_brasil["data"], df_brasil["obitosMM7"],
                     color="lightsalmon", alpha=0.4)
    ax2.set_ylabel("Óbitos diários (MM 7 dias)", color="tab:orange")
    ax2.tick_params(axis="y", labelcolor="tab:orange")

    plt.title("Evolução da COVID-19 no Brasil (2020 – 2025)", fontsize=14, weight="bold")
    plt.grid(alpha=0.3, linestyle="--")
    st.pyplot(fig)

# ==============================================================
# 5. Aba 2 – Município de São Paulo
# ==============================================================

with tabs[1]:
    st.subheader("Município de São Paulo — Casos × Óbitos (MM 7 e 30 dias)")

    df_sp = df[df["municipio"] == "São Paulo"].copy().sort_values("data")
    df_sp = df_sp[
        (df_sp["casosNovos"] < 10000) & (df_sp["obitosNovos"] < 500)
    ]

    df_sp["casosMM7"] = df_sp["casosNovos"].rolling(7, min_periods=1).mean()
    df_sp["casosMM30"] = df_sp["casosNovos"].rolling(30, min_periods=1).mean()
    df_sp["obitosMM7"] = df_sp["obitosNovos"].rolling(7, min_periods=1).mean()
    df_sp["obitosMM30"] = df_sp["obitosNovos"].rolling(30, min_periods=1).mean()

    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df_sp["data"], df_sp["casosMM7"], color="#1565C0", linewidth=2, label="Casos MM7")
    ax1.plot(df_sp["data"], df_sp["casosMM30"], color="#1E88E5", linestyle="--", linewidth=2)
    ax1.set_ylabel("Casos (médias móveis)", color="#1565C0")
    ax2 = ax1.twinx()
    ax2.plot(df_sp["data"], df_sp["obitosMM7"], color="#B71C1C", linewidth=2, label="Óbitos MM7")
    ax2.plot(df_sp["data"], df_sp["obitosMM30"], color="#E64A19", linestyle="--", linewidth=2)
    ax2.set_ylabel("Óbitos (médias móveis)", color="#B71C1C")
    plt.title("Evolução — São Paulo (2020 – 2025)", fontsize=14, weight="bold")
    plt.grid(alpha=0.3, linestyle="--")
    st.pyplot(fig)

# ==============================================================
# 6. Aba 3 – Regiões do Brasil
# ==============================================================

with tabs[2]:
    st.subheader("Casos e Óbitos Totais por Região")

    if "regiao" not in df.columns:
        mapping = {
            "Norte": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
            "Nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
            "Centro-Oeste": ["DF", "GO", "MT", "MS"],
            "Sudeste": ["ES", "MG", "RJ", "SP"],
            "Sul": ["PR", "RS", "SC"],
        }

        def get_region(uf):
            for region, states in mapping.items():
                if uf in states:
                    return region
            return "Desconhecida"

        df["regiao"] = df["estado"].apply(get_region)

    df_region = (
        df.groupby("regiao")[["casosNovos", "obitosNovos"]]
        .sum()
        .sort_values("casosNovos", ascending=False)
        .reset_index()
    )

    df_melt = df_region.melt(id_vars="regiao", var_name="Indicador", value_name="Total")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=df_melt, x="regiao", y="Total",
                hue="Indicador",
                palette={"casosNovos": "steelblue", "obitosNovos": "firebrick"},
                alpha=0.85, ax=ax)
    ax.set_title("Casos e Óbitos Totais por Região", fontsize=13, weight="bold")
    st.pyplot(fig)

# ==============================================================
# 7. Aba 4 – Top Municípios e Estados
# ==============================================================

with tabs[3]:
    st.subheader("Top 10 Municípios e Estados com Mais Casos")

    col1, col2 = st.columns(2)

    with col1:
        top_cities = (
            df.groupby("municipio")["casosAcumulado"]
            .max()
            .sort_values(ascending=False)
            .head(10)
            .sort_values(ascending=True)
        )
        fig1, ax = plt.subplots(figsize=(8, 5))
        bars = ax.barh(top_cities.index, top_cities.values, color="royalblue", alpha=0.85)
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 10000, bar.get_y() + bar.get_height()/2,
                    f"{width:,.0f}", va="center", fontsize=9)
        ax.set_title("Top 10 Municípios com Mais Casos", fontsize=12, weight="bold")
        st.pyplot(fig1)

    with col2:
        df_est = (
            df.groupby("estado")[["obitosAcumulado", "populacaoTCU2019"]]
            .max()
            .assign(
                taxa=lambda d: (d["obitosAcumulado"] / d["populacaoTCU2019"]) * 100000
            )
            .sort_values("obitosAcumulado", ascending=False)
            .head(10)
        )
        fig2, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(data=df_est, x=df_est.index, y="obitosAcumulado",
                    palette="Reds_r", ax=ax)
        ax.set_title("Top 10 Estados com Mais Mortes", fontsize=12, weight="bold")
        plt.xticks(rotation=30)
        st.pyplot(fig2)

# ==============================================================
# 8. Aba 5 – Taxa de Mortalidade
# ==============================================================

with tabs[4]:
    st.subheader("Taxa de Mortalidade — Percentual da População de 2019")

    df_mort = (
        df.groupby("estado")[["obitosAcumulado", "populacaoTCU2019"]]
        .max()
        .assign(taxa_mortalidade=lambda d: (d["obitosAcumulado"] / d["populacaoTCU2019"]) * 100)
        .sort_values("taxa_mortalidade", ascending=False)
        .reset_index()
    )

    media_nac = df_mort["taxa_mortalidade"].mean()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df_mort, x="estado", y="taxa_mortalidade",
                palette="Reds_r", edgecolor="black", alpha=0.9, ax=ax)
    plt.axhline(media_nac, color="gray", linestyle="--", alpha=0.6)
    plt.text(len(df_mort) + 0.2, media_nac,
             f"Média nacional: {media_nac:.2f}%", color="gray", fontsize=10, style="italic")
    ax.set_title("Taxa de Mortalidade por Estado", fontsize=13, weight="bold")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ==============================================================
# Rodapé
# ==============================================================

st.markdown("---")
st.caption("Desenvolvido por Rafael Gallo — Dados: Ministério da Saúde / OpenDataSUS")
