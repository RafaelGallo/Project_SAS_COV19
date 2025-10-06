"""
Módulo responsável pela inicialização da conexão com o banco de dados.

Permite criar ou conectar-se a um banco SQLite local, podendo ser
adaptado facilmente para outros bancos (ex.: PostgreSQL, MySQL).
"""

from sqlalchemy import create_engine


def init_db():
    """
    Inicializa e retorna a conexão com o banco de dados.

    Retorna
    -------
    sqlalchemy.engine.base.Engine
        Objeto Engine do SQLAlchemy, utilizado para operações no banco.
    """

    # Criação da engine de conexão (padrão: SQLite local)
    engine = create_engine("sqlite:///covid19_brasil.db")

    # Mensagem informativa para confirmação da conexão
    print("Conexão com o banco SQLite inicializada com sucesso.")

    return engine
