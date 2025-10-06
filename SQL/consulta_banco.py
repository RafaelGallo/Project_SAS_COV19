"""
Script para salvar o dataset COVID-19 em um banco de dados relacional
utilizando SQLAlchemy.

Compatível com MySQL, PostgreSQL ou outros bancos suportados.
"""

# Instalação de dependências (executar no terminal, não no código):
# pip install sqlalchemy pymysql
# ou, para PostgreSQL:
# pip install sqlalchemy psycopg2

from sqlalchemy import create_engine
import pandas as pd

# ============================================
# Configuração da conexão com o banco de dados
# ============================================

# Exemplo de conexão com MySQL
# Substitua 'usuario' e 'senha' pelos valores reais
engine = create_engine(
    "mysql+pymysql://usuario:senha@localhost:3306/covid19_db",
    echo=False,  # Define True para exibir logs SQL no console
    pool_pre_ping=True  # Verifica conexões antes de reutilizá-las
)

# ============================================
# Escrita dos dados no banco
# ============================================

# Nome da tabela a ser criada ou substituída
table_name = "covid19_dados"

# Envia o DataFrame para o banco de dados
df.to_sql(
    name=table_name,
    con=engine,
    if_exists="replace",  # Substitui tabela existente
    index=False
)

print(f"Dados salvos com sucesso na tabela '{table_name}' do banco MySQL.")
