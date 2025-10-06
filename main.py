"""
Script principal do pipeline ETL COVID-19 Brasil.

Etapas executadas:
1. Extração e transformação dos dados (ETL)
2. Salvamento em formato Parquet
3. Envio para banco de dados SQL
"""

import os
import sys
import pandas as pd

# Adiciona o caminho raiz do projeto para permitir importação de módulos locais
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# Importações de módulos internos
from ETL.etl import executar_etl
from py.save_to_sql import save_to_sql
from base.database import init_db


def main():
    """Função principal que executa o pipeline ETL completo."""
    print("Iniciando pipeline ETL COVID-19 Brasil...\n")

    # Definição dos caminhos de entrada, saída e armazenamento
    base_dir = project_root
    zip_path = os.path.join(base_dir, "input", "HIST_PAINEL_COVIDBR_05set2025.zip")
    extract_path = os.path.join(base_dir, "output")
    parquet_path = os.path.join(base_dir, "data", "HIST_PAINEL_COVIDBR_CONSOLIDADO.parquet")

    # 1. Executar o processo ETL (extração e transformação dos dados)
    print("Executando processo ETL...")
    df_final = executar_etl(zip_path, extract_path)

    # 2. Salvar o resultado consolidado em formato Parquet
    print("\nSalvando dataset consolidado em formato Parquet...")
    df_final.to_parquet(parquet_path, engine="pyarrow", compression="snappy", index=False)
    print(f"Arquivo salvo em: {parquet_path}")
    print(f"Tamanho final: {os.path.getsize(parquet_path) / 1024 / 1024:.2f} MB")

    # 3. Salvar o dataset em banco de dados SQL
    try:
        init_db()  # Inicializa a conexão com o banco
        save_to_sql(df_final)  # Insere os dados na tabela de destino
        print("Dados enviados ao banco SQL com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar no SQL: {e}")

    print("\nPipeline ETL executado com sucesso.")


# Execução direta do script (entry point)
if __name__ == "__main__":
    main()
