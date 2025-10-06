# ================================
# 🐍 Dockerfile — ETL COVID-19 Brasil
# Autor: Rafael Henrique Gallo
# Projeto: Project_SAS_COV19
# ================================

# Imagem base do Python
FROM python:3.10-slim

# Configurações básicas
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    TZ=America/Sao_Paulo

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip \
    wget \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar os arquivos do projeto (ETL e dependências)
COPY . .

# Criar pastas necessárias para ETL
RUN mkdir -p /app/data /app/output /app/ETL

# Comando padrão: executar o pipeline ETL
CMD ["python", "main.py"]
