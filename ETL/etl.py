"""
Módulo de execução do processo ETL (Extract, Transform, Load)
para os dados da COVID-19 no Brasil.

Etapas:
1. Extração dos arquivos CSV de um arquivo ZIP.
2. Leitura incremental e concatenação dos CSVs.
3. Limpeza e padronização dos dados.
4. Retorno de um DataFrame consolidado.
"""

import os
import glob
import zipfile
import pandas as pd
from tqdm import tqdm


def executar_etl(zip_path, extract_path):
    """
    Executa o processo ETL completo dos dados COVID-19.

    Parâmetros
    ----------
    zip_path : str
        Caminho completo para o arquivo ZIP contendo os CSVs.
    extract_path : str
        Diretório onde os arquivos serão extraídos.

    Retorna
    -------
    pandas.DataFrame
        DataFrame consolidado e tratado com todos os registros.
    """

    # 1. Extração dos arquivos ZIP
    print(f"Extraindo arquivos de: {zip_path}")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"Extração concluída. Arquivos salvos em: {extract_path}")

    # 2. Leitura dos arquivos CSV extraídos
    csv_files = glob.glob(os.path.join(extract_path, "HIST_PAINEL_COVIDBR_*.csv"))
    print(f"{len(csv_files)} arquivos CSV encontrados.\n")

    dfs = []
    for file in tqdm(csv_files, desc="Lendo arquivos CSV", unit="arquivo"):
        df = pd.read_csv(file, sep=";", encoding="utf-8", low_memory=False)
        dfs.append(df)

    # Concatena todos os arquivos em um único DataFrame
    df_final = pd.concat(dfs, ignore_index=True)

    # 3. Conversão de datas e ordenação
    df_final["data"] = pd.to_datetime(df_final["data"], errors="coerce")
    df_final.sort_values(by=["estado", "municipio", "data"], inplace=True)

    # 4. Preenchimento de campos categóricos ausentes
    df_final["estado"].fillna("BR", inplace=True)
    df_final["municipio"].fillna("Não informado", inplace=True)
    df_final["nomeRegiaoSaude"].fillna("Ignorado", inplace=True)
    df_final["codRegiaoSaude"].fillna(-1, inplace=True)
    df_final["interior/metropolitana"] = (
        df_final["interior/metropolitana"].astype(str).fillna("Ignorado")
    )

    # 5. Preenchimento da população média por estado
    df_final["populacaoTCU2019"] = (
        df_final.groupby("estado")["populacaoTCU2019"]
        .transform(lambda x: x.fillna(x.median()))
    )

    # 6. Substituição de valores nulos nas colunas numéricas
    for col in ["casosAcumulado", "casosNovos", "obitosAcumulado", "obitosNovos"]:
        df_final[col] = df_final[col].fillna(0)

    # 7. Remoção de colunas irrelevantes
    df_final.drop(
        columns=["Recuperadosnovos", "emAcompanhamentoNovos", "codmun"],
        inplace=True,
        errors="ignore"
    )

    # 8. Resumo informativo
    print("\nResumo do dataset processado:")
    print(f"Período: {df_final['data'].min().date()} → {df_final['data'].max().date()}")
    print(f"Estados únicos: {df_final['estado'].nunique()}")
    print(f"Municípios únicos: {df_final['municipio'].nunique()}")
    print(f"Total de linhas: {len(df_final):,}")

    return df_final
