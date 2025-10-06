# 🧬 Project SAS-COV19 — COVID-19 Data Analytics & Forecast Dashboard  

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-success)
![Seaborn](https://img.shields.io/badge/Seaborn-Data%20Viz-lightblue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📘 **Descrição do Projeto**

O **Project SAS-COV19** é um sistema analítico completo para **monitoramento, análise e previsão da pandemia de COVID-19 no Brasil (2020–2025)**.  

O projeto realiza:
- Limpeza e integração de bases públicas (Ministério da Saúde e OWID);
- Cálculo de **médias móveis** e indicadores epidemiológicos;
- Identificação de **ondas pandêmicas** e períodos de endemia;
- Modelagem preditiva com **Regressão Polinomial e Logística**;
- Visualização interativa via **Streamlit Dashboard**.

O objetivo é fornecer uma visão exploratória e preditiva do comportamento da pandemia no Brasil e em suas regiões, com foco em políticas públicas, análises epidemiológicas e estudos de tendência.

## 🧩 **Arquitetura do Projeto**

```
Project_SAS_COV19/
│
├── app/               # Aplicação Streamlit (dashboard)
├── base/              # Funções base e utilitários de data processing
├── data/              # Dados brutos e tratados
├── docker/            # Arquivos de containerização
├── ETL/               # Scripts de extração, transformação e carga
├── img/               # Gráficos gerados para documentação
├── input/             # Dados de entrada (csv, json, etc.)
├── models/            # Modelos de previsão e machine learning
├── notebook/          # Jupyter Notebooks de análise exploratória
├── output/            # Resultados e gráficos processados
├── py/                # Scripts Python auxiliares
├── src/               # Código-fonte principal
│
├── main.py            # Script principal de execução
├── models.py          # Modelos de regressão e previsões
├── save_to_sql.py     # Exportação dos resultados para banco SQL
├── serializers.py     # Serialização de modelos e resultados
├── settings.py        # Configurações globais do projeto
├── views.py           # Camada de visualização
├── requirements.txt   # Dependências do projeto
├── README.md          # Este arquivo
└── LICENSE
````

## 🧮 **Principais Funcionalidades**

| Categoria | Descrição |
|------------|------------|
| 🧹 **ETL & Limpeza de Dados** | Correção de outliers, normalização e integração de fontes. |
| 📊 **Visualização Exploratória** | Gráficos dinâmicos (casos, óbitos, letalidade, mortalidade). |
| 🗺️ **Análise Regional e Temporal** | Comparações entre estados, regiões e ondas pandêmicas. |
| 📈 **Modelos de Previsão** | Regressão Polinomial e Logística aplicadas a séries temporais. |
| 🧠 **Análise Preditiva** | Estimativas futuras de casos acumulados e tendência de saturação. |
| 🧩 **Dashboard Streamlit** | Interface visual para análise interativa e relatórios automáticos. |

## 🚀 **Destaques do Projeto**

### 🔹 Evolução Nacional — Casos x Óbitos
![Evolução Nacional](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/1.png)

### 🔹 Ondas Epidêmicas no Brasil
![Ondas Epidêmicas](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/2.png)

### 🔹 Município de São Paulo
![SP Casos](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/3.png)

### 🔹 Casos e Óbitos por Região
![Regiões](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/4.png)

### 🔹 Tendência Nacional (MM30)
![Tendência Nacional](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/5.png)

### 🔹 Taxa de Letalidade (% entre Casos Confirmados)
![Letalidade](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/6.png)

### 🔹 Top 10 Estados com Mais Mortes
![Top 10 Mortes](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/7.png)

### 🔹 Taxa de Mortalidade (População 2019)
![Mortalidade](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/8.png)

### 🔹 Dashboard Streamlit
![Dashboard](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/9.png)

## 📈 **Modelos de Previsão**

### 🧮 Regressão Polinomial
Captura a tendência de crescimento e desaceleração dos casos acumulados ao longo do tempo.

\[y = \beta_0 + \beta_1x + \beta_2x^2 + \dots + \beta_nx^n\]

### 🧬 Regressão Logística
Modela a saturação da curva de crescimento, representando a limitação populacional de contágio.

\[
y = \frac{1}{1 + e^{-(\beta_0 + \beta_1x)}}
\]

Ambos os modelos foram avaliados com dados de 2020–2025, utilizando:
- Normalização MinMaxScaler;
- Ajuste de curva por otimização de mínimos quadrados;
- Comparação de erro (MAE e RMSE) para análise de acurácia.

## 🖥️ **Tecnologias Utilizadas**

| Categoria | Ferramentas |
|------------|-------------|
| Linguagem | Python 3.10 |
| Data Science | Pandas, NumPy, SciPy |
| Visualização | Matplotlib, Seaborn |
| Machine Learning | scikit-learn |
| Dashboard | Streamlit |
| Banco de Dados | SQL (via `save_to_sql.py`) |
| Ambiente | Docker, Jupyter Notebook |

## 🧠 **Insights Principais**

- O Brasil apresentou **5 ondas epidêmicas principais**, com pico máximo em **fev/2021**.  
- A transição para **endemia** ocorre em meados de **2023**, com estabilização de casos.  
- As **regiões Sudeste e Nordeste** concentraram >60% dos casos nacionais.  
- O **Piauí** apresentou a **maior taxa de letalidade (8,2%)**.  
- A mortalidade por população foi maior no **Distrito Federal e Roraima**.

## 📦 **Instalação e Execução**

```bash
# Clonar o repositório
git clone https://github.com/RafaelGallo/Project_SAS_COV19.git
cd Project_SAS_COV19

# Instalar dependências
pip install -r requirements.txt

# Rodar o dashboard
streamlit run app/main.py
````

## 📊 **Resultados Esperados**

* Visualizações limpas e consistentes das séries temporais COVID-19 (2020–2025).
* Painel interativo para navegação por região, estado ou município.
* Modelos preditivos ajustados à realidade epidemiológica brasileira.
* Possibilidade de exportar relatórios e análises em formato `.csv` e `.png`.

## 🧾 **Licença**

Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 **Autor**

**Rafael Henrique Gallo**
📍 Cientista de Dados • MBA Data Science & IA — FIAP
📧 [rafaelgallo.ds@gmail.com](mailto:rafaelgallo.ds@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/rafaelhenriquegallo)
🌐 [Kaggle](https://www.kaggle.com/rafaelgallo)


> “Ciência de Dados é o elo entre informação e decisão. — *Rafael Gallo*”
