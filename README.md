# 🧬 Project SAS-COV19 — COVID-19 Data Analytics & Forecast Dashboard  

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-success)
![Seaborn](https://img.shields.io/badge/Seaborn-Data%20Viz-lightblue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

![](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/log.jpg?raw=true)

## 📘 **Descrição do Projeto**

O **Project SAS-COV19** é um sistema analítico completo para **monitoramento, análise e previsão da pandemia de COVID-19 no Brasil (2020–2025)**.  

O projeto realiza:
- Extração automática e integração de bases públicas ([covid.saude.gov.br](https://covid.saude.gov.br/));
- Limpeza e unificação via pipeline **ETL** automatizado (`main.py`);
- Cálculo de **médias móveis**, indicadores epidemiológicos e regionais;
- Identificação de **ondas pandêmicas** e fases de endemia;
- Modelagem preditiva com **Regressão Polinomial e Logística**;
- Visualização interativa via **Streamlit Dashboard**.

O objetivo é fornecer uma visão exploratória e preditiva do comportamento da pandemia no Brasil e em suas regiões, com foco em políticas públicas, análises epidemiológicas e estudos de tendência.

## 🧩 **Arquitetura do Projeto**

````
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
├── main.py            # Script principal de execução (ETL completo)
├── models.py          # Modelos de regressão e previsões
├── save_to_sql.py     # Exportação dos resultados para banco SQL
├── serializers.py     # Serialização de modelos e resultados
├── settings.py        # Configurações globais do projeto
├── views.py           # Camada de visualização
├── requirements.txt   # Dependências do projeto
├── README.md          # Este arquivo
└── LICENSE
````


## ⚙️ **Pipeline ETL — Extração, Transformação e Carga**

> **Responsável:** Rafael Henrique Gallo  
> **Descrição:** O arquivo `main.py` realiza a **automação completa** do fluxo de dados COVID-19 do Ministério da Saúde.

### 📋 **Etapas Principais**
1. Detecta automaticamente o arquivo `.zip` mais recente na pasta de dados;  
2. Extrai e lê os arquivos `HIST_PAINEL_COVIDBR_*.csv`;  
3. Realiza limpeza e padronização de colunas e valores ausentes;  
4. Consolida todos os arquivos em um único CSV:  
   `COVIDBR_2020_2025_Consolidado.csv`.  

### 🔧 **Execução**
```bash
python main.py
````

### 🧩 **Fontes de Dados**

* [Portal COVID-19 do Ministério da Saúde](https://covid.saude.gov.br/)
* [Brasil.io - Casos e Óbitos](https://brasil.io/dataset/covid19/caso_full/)
* [Our World in Data (Brasil)](https://ourworldindata.org/coronavirus/country/brazil)

## 🧮 **Principais Funcionalidades**

| Categoria                           | Descrição                                                          |
| ----------------------------------- | ------------------------------------------------------------------ |
| 🧹 **ETL & Limpeza de Dados**       | Correção de outliers, normalização e integração de fontes.         |
| 📊 **Visualização Exploratória**    | Gráficos dinâmicos (casos, óbitos, letalidade, mortalidade).       |
| 🗺️ **Análise Regional e Temporal** | Comparações entre estados, regiões e ondas pandêmicas.             |
| 📈 **Modelos de Previsão**          | Regressão Polinomial e Logística aplicadas a séries temporais.     |
| 🧠 **Análise Preditiva**            | Estimativas futuras de casos acumulados e tendência de saturação.  |
| 🧩 **Dashboard Streamlit**          | Interface visual para análise interativa e relatórios automáticos. |

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

![Ajuste Polinomial](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/10.png)

### 🔹 **Projeção Futura de Casos (10 Semanas)**

Estimativa de novas infecções com base na regressão polinomial de grau 7.

![Previsão Futura](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/11.png)

### 🧬 Regressão Logística

Modela a saturação da curva de crescimento (efeito platô de óbitos acumulados).

![Modelo Logístico](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/12.png)

## 📈 Modelos de Previsão

### 🧮 Regressão Polinomial (grau p)
Estimamos a tendência dos **casos novos** ao longo do tempo com um polinômio de grau *p*:

$$
\hat{y}(x) = \sum_{k=0}^{p} \beta_k \, x^{k}
$$

> No projeto, usamos tipicamente \(p=7\) para capturar curvaturas sem sobreajuste excessivo.

---

### 🧬 Modelo Logístico (crescimento acumulado)
Para **casos/óbitos acumulados**, modelamos a curva-S com saturação:

$$
\hat{Y}(t) = \frac{K}{1 + \exp\!\big(-r\,(t - t_{0})\big)}
$$

onde \(K\) é a **capacidade de carga** (platô), \(r\) a **taxa de crescimento** e \(t_{0}\) o **ponto de inflexão**.


## 🧠 **Insights Principais**

* O Brasil apresentou **5 ondas epidêmicas principais**, com pico máximo em **fev/2021**;
* A transição para **endemia** ocorre em **2023**, com estabilização de casos;
* As **regiões Sudeste e Nordeste** concentraram mais de 60% dos casos nacionais;
* O **Piauí** teve a **maior taxa de letalidade (8,2%)**;
* A mortalidade proporcional à população foi mais alta no **Distrito Federal** e em **Roraima**.

## 🖥️ **Tecnologias Utilizadas**

| Categoria        | Ferramentas              |
| ---------------- | ------------------------ |
| Linguagem        | Python 3.10              |
| Data Science     | Pandas, NumPy, SciPy     |
| Visualização     | Matplotlib, Seaborn      |
| Machine Learning | scikit-learn             |
| Dashboard        | Streamlit                |
| Banco de Dados   | SQL                      |
| Automação        | tqdm, zipfile, glob      |
| Ambiente         | Docker, Jupyter Notebook |

## 📦 **Instalação e Execução**

```bash
# Clonar o repositório
git clone https://github.com/RafaelGallo/Project_SAS_COV19.git
cd Project_SAS_COV19

# Instalar dependências
pip install -r requirements.txt

# Rodar pipeline ETL
python main.py

# Rodar dashboard interativo
streamlit run app/main.py
```
## 📊 **Resultados Esperados**

* Visualizações limpas e consistentes das séries temporais COVID-19 (2020–2025);
* Painel interativo para análise por região, estado e município;
* Modelos preditivos realistas e ajustados à série histórica;
* Exportação de relatórios e gráficos em `.csv` e `.png`.

## 🧾 **Citação**

> “Dados oficiais extraídos do [Portal COVID-19 do Ministério da Saúde](https://covid.saude.gov.br/),
> tratados, consolidados e modelados via pipeline ETL e regressões polinomial/logística
> desenvolvidas por **Rafael Henrique Gallo (2025)**.”

## 👨‍💻 **Autor**

**Rafael Henrique Gallo**

📍 Cientista de Dados • MBA Data Science & IA — FIAP
📧 [rafaelgallo.ds@gmail.com](mailto:rafaelgallo.ds@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/rafaelhenriquegallo)
🌐 [Kaggle](https://www.kaggle.com/rafaelgallo)

> 🧩 *“Ciência de Dados é o elo entre informação e decisão.” — Rafael Gallo*
