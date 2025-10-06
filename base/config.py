"""
Módulo de configuração de caminhos e constantes do projeto COVID-19.

Contém definições centrais utilizadas em diferentes etapas do pipeline ETL:
- Diretórios base (dados, saída, banco de dados)
- Caminhos de arquivos consolidados
- Nome padrão da tabela SQL
"""

import os

# ============================================
# Diretório base do projeto
# ============================================

BASE_DIR = r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\covid19_SP\SaS_Cov19_project"

# ============================================
# Caminhos principais
# ============================================

# Diretório que armazena os arquivos de dados (.csv, .parquet, .db)
DATA_PATH = os.path.join(BASE_DIR, "data")

# Diretório de saída utilizado para arquivos processados
OUTPUT_PATH = os.path.join(BASE_DIR, "output")

# Caminho completo do banco de dados local (SQLite)
DB_PATH = os.path.join(DATA_PATH, "covid19_brasil.db")

# ============================================
# Arquivos principais de dados
# ============================================

# Arquivo consolidado em formato CSV
CSV_FILE = os.path.join(DATA_PATH, "HIST_PAINEL_COVIDBR_CONSOLIDADO.csv")

# Arquivo consolidado em formato Parquet
PARQUET_FILE = os.path.join(DATA_PATH, "HIST_PAINEL_COVIDBR_CONSOLIDADO.parquet")

# ============================================
# Configuração padrão de banco de dados
# ============================================

# Nome padrão da tabela a ser criada ou substituída no SQL
TABLE_NAME = "covid19_dados"
