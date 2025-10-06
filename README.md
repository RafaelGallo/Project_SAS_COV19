# 🧬 Project SAS-COV19 — COVID-19 Data Analytics & Forecast Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-success)
![Seaborn](https://img.shields.io/badge/Seaborn-Data%20Viz-lightblue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

![](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/log.jpg?raw=true)

## 📘 **Project Overview**

**Project SAS-COV19** is a complete analytical system for **monitoring, analyzing, and forecasting the COVID-19 pandemic in Brazil (2020–2025)**.

The project performs:

* Automatic extraction and integration of public datasets ([covid.saude.gov.br](https://covid.saude.gov.br/));
* Cleaning and consolidation through an automated **ETL pipeline** (`main.py`);
* Calculation of **moving averages** and epidemiological indicators;
* Identification of **pandemic waves** and endemic transition phases;
* Predictive modeling using **Polynomial and Logistic Regression**;
* Interactive visualization through a **Streamlit Dashboard**.

The goal is to provide an exploratory and predictive view of the pandemic’s behavior in Brazil and its regions — supporting public policy, epidemiological research, and trend analysis.

## 🌍 Extensions & Related Projects

As part of the **analytical ecosystem of Project SAS-COV19**, new modules and complementary studies are being developed, focusing on **time series, vaccination data, adverse effects, and natural language processing (NLP)** related to the global pandemic.

### 🧠 **Expansion Projects**

| Category                                           | Description                                                                                   | Dataset Source                                                                                                                       | Project Folder |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| 💉 **COVID-19 Post Vaccination Statewide Stats**   | Time series analysis and modeling of post-vaccination data (cases, hospitalizations, deaths). | [Kaggle Dataset](https://www.kaggle.com/datasets/tdison/covid19-post-vaccination-statewide-stats)                                    |                |
| 🧬 **COVID-19 Vaccine Adverse Reactions (World)**  | Temporal study of vaccine adverse reactions by country, age group, and manufacturer.          | [Kaggle Dataset](https://www.kaggle.com/datasets/ayushggarg/covid19-vaccine-adverse-reactions)                                       |                |
| 🧫 **COVID-19 Vaccination Effects (Impact Study)** | Comparative analysis between vaccination rates and epidemiological indicators.                | [Kaggle Dataset](https://www.kaggle.com/datasets/telikaramu/covid-19-vaccination-effects)                                            |                |
| 🏙️ **COVID-19 Vaccination in Tiered Cities**      | Time series of vaccination data in cities with different infrastructure levels.               | [Kaggle Dataset](https://www.kaggle.com/datasets/achintsoni/covid19-vaccination-data-for-different-tier-cities)                      |                |
| 📰 **COVID-19 Fake News Detection (NLP)**          | Automatic classification of misinformation using BERT and LLM-based models.                   | [Kaggle Dataset](https://www.kaggle.com/datasets/elvinagammed/covid19-fake-news-dataset-nlp/code?datasetId=1207011&sortBy=voteCount) |                |
| 🐦 **Global COVID-19 X (Twitter) Analysis (NLP)**  | Sentiment, topic, and fake news detection in global COVID-19 tweets.                          | [Kaggle Dataset](https://www.kaggle.com/datasets/rohitashchandra/global-covid19-twitter-dataset?select=Brazil.csv)                   |                |

> 🔗 These modules are part of the **“SAS-COV19 Global Analysis”** series, integrating epidemiological, behavioral, and media data to understand the direct and indirect impacts of the pandemic worldwide.

## 🌐 Next Steps

🚧 **In development:**

* LSTM and Prophet models for vaccination and adverse reaction time series forecasting.
* Dedicated Streamlit dashboards for each module (Vaccination, Reactions, Fake News, Twitter NLP).
* Integration with international databases (OWID, WHO, Kaggle).
* Unified repository: **SAS-COV19 Global Analytics Suite**.

## 🧩 **Project Architecture**

```
Project_SAS_COV19/
│
├── app/               # Streamlit application (dashboard)
├── base/              # Base functions and data processing utilities
├── data/              # Raw and processed data
├── docker/            # Containerization files
├── ETL/               # Extraction, Transformation, and Load scripts
├── img/               # Generated charts and documentation images
├── input/             # Input datasets (csv, json, etc.)
├── models/            # Forecasting and ML models
├── notebook/          # Exploratory Jupyter notebooks
├── output/            # Processed outputs and visualizations
├── py/                # Auxiliary Python scripts
├── src/               # Core source code
│
├── main.py            # Main ETL execution script
├── models.py          # Regression and forecast models
├── save_to_sql.py     # SQL database export
├── serializers.py     # Model/result serialization
├── settings.py        # Global configuration
├── views.py           # Visualization layer
├── requirements.txt   # Project dependencies
├── README.md          # This file
└── LICENSE
```

## ⚙️ **ETL Pipeline — Extraction, Transformation & Load**

> **Author:** Rafael Henrique Gallo
> **Description:** The `main.py` file automates the entire COVID-19 data pipeline from the Brazilian Ministry of Health.

### 📋 **Main Steps**

1. Automatically detects the latest `.zip` file in the data directory;
2. Extracts and reads all `HIST_PAINEL_COVIDBR_*.csv` files;
3. Cleans and standardizes columns and missing values;
4. Consolidates all datasets into a single CSV:
   `COVIDBR_2020_2025_Consolidado.csv`.

### 🔧 **Execution**

```bash
python main.py
```

### 🧩 **Data Sources**

* [Ministry of Health — COVID-19 Portal](https://covid.saude.gov.br/)
* [Brasil.io - COVID-19 Cases and Deaths](https://brasil.io/dataset/covid19/caso_full/)
* [Our World in Data (Brazil)](https://ourworldindata.org/coronavirus/country/brazil)

## 🧮 **Main Features**

| Category                             | Description                                                      |
| ------------------------------------ | ---------------------------------------------------------------- |
| 🧹 **ETL & Data Cleaning**           | Outlier correction, normalization, and multi-source integration. |
| 📊 **Exploratory Visualization**     | Dynamic charts (cases, deaths, lethality, mortality).            |
| 🗺️ **Regional & Temporal Analysis** | Comparison between states, regions, and pandemic waves.          |
| 📈 **Forecast Models**               | Polynomial and Logistic Regression applied to time series.       |
| 🧠 **Predictive Analysis**           | Future estimates of accumulated cases and saturation trends.     |
| 🧩 **Streamlit Dashboard**           | Interactive interface for analysis and automated reports.        |

## 🚀 **Project Highlights**

### 🔹 National Evolution — Cases vs Deaths

![Evolução Nacional](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/1.png)

### 🔹 Epidemic Waves in Brazil

![Ondas Epidêmicas](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/2.png)

### 🔹 São Paulo Municipality

![SP Casos](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/3.png)

### 🔹 Cases and Deaths by Region

![Regiões](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/4.png)

### 🔹 National Trend (30-day MA)

![Tendência Nacional](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/5.png)

### 🔹 Lethality Rate (% of Confirmed Cases)

![Letalidade](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/6.png)

### 🔹 Top 10 States by Deaths

![Top 10 Mortes](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/7.png)

### 🔹 Mortality Rate (2019 Population)

![Mortalidade](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/8.png)

### 🔹 Streamlit Dashboard

![Dashboard](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/9.png)

## 📈 **Forecasting Models**

### 🧮 Polynomial Regression (degree p)

We estimate the trend of **new cases** over time using a polynomial of degree *p*:

$$
\hat{y}(x) = \sum_{k=0}^{p} \beta_k , x^{k}
$$

> In this project, (p = 7) is commonly used to smooth the curve and capture curvature without overfitting.

### 🧬 Logistic Growth Model (accumulated cases)

For **accumulated cases or deaths**, we model the S-shaped curve with saturation:

$$
\hat{Y}(t) = \frac{K}{1 + \exp!\big(-r,(t - t_{0})\big)}
$$

Where (K) is the **carrying capacity** (plateau), (r) the **growth rate**, and (t_{0}) the **inflection point**.

### 📊 Model Visualizations

#### Polynomial Regression Fit

![Ajuste Polinomial](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/10.png)

#### 10-Week Forecast Projection

![Previsão Futura](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/11.png)

#### Logistic Growth — Accumulated Deaths

![Modelo Logístico](https://github.com/RafaelGallo/Project_SAS_COV19/blob/main/img/12.png)

## 🧠 **Key Insights**

* Brazil experienced **5 major epidemic waves**, peaking in **February 2021**;
* The transition to **endemic status** occurred in **2023**, with case stabilization;
* The **Southeast and Northeast** regions accounted for over 60% of national cases;
* **Piauí** had the **highest lethality rate (8.2%)**;
* Mortality relative to population was highest in **Distrito Federal** and **Roraima**.

## 🖥️ **Technologies Used**

| Category         | Tools                    |
| ---------------- | ------------------------ |
| Language         | Python 3.10              |
| Data Science     | Pandas, NumPy, SciPy     |
| Visualization    | Matplotlib, Seaborn      |
| Machine Learning | scikit-learn             |
| Dashboard        | Streamlit                |
| Database         | SQL                      |
| Automation       | tqdm, zipfile, glob      |
| Environment      | Docker, Jupyter Notebook |

## 📦 **Installation & Execution**

```bash
# Clone repository
git clone https://github.com/RafaelGallo/Project_SAS_COV19.git
cd Project_SAS_COV19

# Install dependencies
pip install -r requirements.txt

# Run ETL pipeline
python main.py

# Launch interactive dashboard
streamlit run app/main.py
```

## 📊 **Expected Results**

* Clean and consistent visualizations of COVID-19 time series (2020–2025);
* Interactive dashboard for analysis by region, state, and municipality;
* Predictive models aligned with real-world epidemiological behavior;
* Export reports and visualizations in `.csv` and `.png` formats.

## 🧾 **Citation**

> “Official data extracted from the [COVID-19 Portal of the Brazilian Ministry of Health](https://covid.saude.gov.br/),
> cleaned, consolidated, and modeled via ETL pipeline and polynomial/logistic regressions
> developed by **Rafael Henrique Gallo (2025)**.”

## 👨‍💻 **Author**

**Rafael Henrique Gallo**

📍 Data Scientist • MBA in Data Science & AI — FIAP
📧 [rafaelgallo.ds@gmail.com](mailto:rafaelgallo.ds@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/rafaelhenriquegallo)
🌐 [Kaggle](https://www.kaggle.com/rafaelgallo)

> 🧩 *“Data Science is the bridge between information and decision.” — Rafael Gallo*

