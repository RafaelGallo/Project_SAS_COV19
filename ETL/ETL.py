"""
ETL (Extract, Transform, Load) module for processing COVID-19 data in Brazil.

Steps:
1. Extract CSV files from a ZIP archive.
2. Incrementally read and concatenate the CSV files.
3. Clean and standardize the dataset.
4. Return a consolidated Pandas DataFrame.
"""

import os
import glob
import zipfile
import pandas as pd
from tqdm import tqdm


def run_etl(zip_path: str, extract_path: str) -> pd.DataFrame:
    """
    Executes the complete ETL (Extract, Transform, Load) process
    for the Brazilian COVID-19 dataset.

    Parameters
    ----------
    zip_path : str
        Full path to the ZIP file containing the CSVs.
    extract_path : str
        Directory where the files will be extracted.

    Returns
    -------
    pandas.DataFrame
        Consolidated and cleaned DataFrame containing all records.
    """

    # 1. Extract files from the ZIP archive
    print(f"Extracting files from: {zip_path}")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"Extraction completed. Files saved to: {extract_path}")

    # 2. Read all extracted CSV files
    csv_files = glob.glob(os.path.join(extract_path, "HIST_PAINEL_COVIDBR_*.csv"))
    print(f"{len(csv_files)} CSV files found.\n")

    dfs = []
    for file in tqdm(csv_files, desc="Reading CSV files", unit="file"):
        df = pd.read_csv(file, sep=";", encoding="utf-8", low_memory=False)
        dfs.append(df)

    # Concatenate all DataFrames into one
    df_final = pd.concat(dfs, ignore_index=True)

    # 3. Convert date column and sort by state, city, and date
    df_final["data"] = pd.to_datetime(df_final["data"], errors="coerce")
    df_final.sort_values(by=["estado", "municipio", "data"], inplace=True)

    # 4. Fill missing categorical fields
    df_final["estado"].fillna("BR", inplace=True)
    df_final["municipio"].fillna("Not informed", inplace=True)
    df_final["nomeRegiaoSaude"].fillna("Unknown", inplace=True)
    df_final["codRegiaoSaude"].fillna(-1, inplace=True)
    df_final["interior/metropolitana"] = (
        df_final["interior/metropolitana"].astype(str).fillna("Unknown")
    )

    # 5. Fill population column using median per state
    df_final["populacaoTCU2019"] = (
        df_final.groupby("estado")["populacaoTCU2019"]
        .transform(lambda x: x.fillna(x.median()))
    )

    # 6. Replace nulls in numerical columns
    for col in ["casosAcumulado", "casosNovos", "obitosAcumulado", "obitosNovos"]:
        df_final[col] = df_final[col].fillna(0)

    # 7. Drop irrelevant columns if they exist
    df_final.drop(
        columns=["Recuperadosnovos", "emAcompanhamentoNovos", "codmun"],
        inplace=True,
        errors="ignore"
    )

    # 8. Display summary
    print("\nDataset summary:")
    print(f"Period: {df_final['data'].min().date()} → {df_final['data'].max().date()}")
    print(f"Unique states: {df_final['estado'].nunique()}")
    print(f"Unique cities: {df_final['municipio'].nunique()}")
    print(f"Total rows: {len(df_final):,}")

    return df_final
