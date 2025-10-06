"""
Módulo para salvar um DataFrame em um banco de dados SQL.

Compatível com SQLite, PostgreSQL, MySQL e outros bancos suportados
pelo SQLAlchemy.
"""

import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm


def save_to_sql(df):
    """
    Salva um DataFrame em um banco de dados SQL.

    Parâmetros
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados a serem salvos.

    Notas
    -----
    - O banco padrão utilizado é SQLite (arquivo local).
    - Pode ser facilmente adaptado para PostgreSQL ou MySQL
      alterando a string de conexão no create_engine().
    """

    # Criação da conexão com o banco SQLite local
    engine = create_engine("sqlite:///covid19_brasil.db")

    # Nome da tabela de destino no banco
    table_name = "covid19_painel"

    # Define o tamanho dos blocos para inserção incremental
    chunk_size = 50_000

    print(f"Salvando {len(df):,} registros na tabela '{table_name}' "
          f"em blocos de {chunk_size} linhas...")

    # Inserção dos dados em blocos (chunks)
    for i in tqdm(range(0, len(df), chunk_size),
                  desc="Enviando ao banco SQL",
                  unit="chunk"):
        df.iloc[i:i + chunk_size].to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False
        )

    print(f"Dados salvos com sucesso no banco SQLite (covid19_brasil.db).")
