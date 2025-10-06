"""
Script para exportar o dataset COVID-19 Brasil para um banco de dados SQLite.

Etapas executadas:
1. Ler o arquivo CSV ou Parquet consolidado.
2. Criar (ou conectar a) um banco SQLite local.
3. Salvar os dados em uma tabela.
"""

import os
import sqlite3
import pandas as pd


# ============================================
# Configurações de caminho
# ============================================

# Diretório base onde os dados estão armazenados
DATA_PATH = r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\covid19_SP\SaS_Cov19_project\data"

# Caminhos completos dos arquivos
CSV_FILE = os.path.join(DATA_PATH, "HIST_PAINEL_COVIDBR_CONSOLIDADO.csv")
DB_FILE = os.path.join(DATA_PATH, "covid19_brasil.db")

print("Iniciando exportação para banco SQLite...")

# ============================================
# Leitura do dataset consolidado
# ============================================

if os.path.exists(CSV_FILE):
    # Lê o arquivo CSV consolidado
    print(f"Lendo arquivo CSV: {CSV_FILE}")
    df = pd.read_csv(CSV_FILE, sep=';', encoding='utf-8')
else:
    # Caso o CSV não exista, tenta ler o equivalente em Parquet
    parquet_file = CSV_FILE.replace('.csv', '.parquet')
    print(f"Lendo arquivo Parquet: {parquet_file}")
    df = pd.read_parquet(parquet_file)

# ============================================
# Criação do banco de dados SQLite
# ============================================

# Conecta (ou cria) o arquivo de banco de dados
conn = sqlite3.connect(DB_FILE)
print(f"Banco criado ou conectado em: {DB_FILE}")

# ============================================
# Escrita da tabela
# ============================================

tabela = "covid19_dados"

# Salva o DataFrame como tabela no banco SQLite
df.to_sql(tabela, conn, if_exists="replace", index=False)
print(f"Tabela '{tabela}' salva com sucesso no banco SQLite.")

# ============================================
# Encerramento da conexão
# ============================================

# Confirma a transação e fecha a conexão
conn.commit()
conn.close()

# ============================================
# Resumo final
# ============================================

print("Exportação concluída com sucesso.")
print(f"Total de linhas inseridas: {len(df):,}")
