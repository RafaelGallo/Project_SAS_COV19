"""
COVID-19 Brazil Data Consolidation Pipeline

Steps:
1. Locate the most recent ZIP file in the data directory.
2. Extract and read all contained CSV files.
3. Clean and standardize the dataset.
4. Save the unified dataset as a consolidated CSV file.
"""

import os
import zipfile
import glob
import pandas as pd
from tqdm import tqdm

# ==============================================================
# Paths configuration
# ==============================================================
data_dir = r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\covid19_SP\data"
extract_path = r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\covid19_SP\SaS_Cov19_project\output\COVIDBR"
output_csv = os.path.join(extract_path, "COVIDBR_2020_2025_Consolidated.csv")

# ==============================================================
# Locate the most recent ZIP file automatically
# ==============================================================
zip_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".zip")]
if not zip_files:
    raise FileNotFoundError("No ZIP files found in the specified directory.")

zip_path = max(zip_files, key=os.path.getmtime)
print(f"Detected ZIP file: {os.path.basename(zip_path)}")

# ==============================================================
# Extract files
# ==============================================================
print(f"Extracting files to {extract_path} ...")
os.makedirs(extract_path, exist_ok=True)
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_path)
print("Extraction completed.")

# ==============================================================
# Locate all extracted CSV files
# ==============================================================
csv_files = glob.glob(os.path.join(extract_path, "HIST_PAINEL_COVIDBR_*.csv"))
print(f"{len(csv_files)} CSV files found:")
for f in csv_files:
    print(" -", os.path.basename(f))

# ==============================================================
# Read and combine all CSVs
# ==============================================================
dfs = []
for file in csv_files:
    print(f"Reading {os.path.basename(file)} ...")
    df = pd.read_csv(file, sep=";", encoding="utf-8", low_memory=False)
    dfs.append(df)

df_final = pd.concat(dfs, ignore_index=True)
print(f"Unified dataset: {df_final.shape[0]:,} rows × {df_final.shape[1]} columns.".replace(",", "."))

# ==============================================================
# Data cleaning and standardization
# ==============================================================
df_final["data"] = pd.to_datetime(df_final["data"], errors="coerce")
df_final.sort_values(by=["estado", "municipio", "data"], inplace=True)

df_final["estado"].fillna("BR", inplace=True)
df_final["municipio"].fillna("Not informed", inplace=True)
df_final["nomeRegiaoSaude"].fillna("Unknown", inplace=True)
df_final["codRegiaoSaude"].fillna(-1, inplace=True)
df_final["interior/metropolitana"].fillna("Unknown", inplace=True)

# Fill population using the median per state
df_final["populacaoTCU2019"] = (
    df_final.groupby("estado")["populacaoTCU2019"]
    .transform(lambda x: x.fillna(x.median()))
)

# Replace NaNs in case and death counts with zeros
for col in ["casosAcumulado", "casosNovos", "obitosAcumulado", "obitosNovos"]:
    if col in df_final.columns:
        df_final[col] = df_final[col].fillna(0)

# Remove irrelevant columns if present
cols_to_drop = [c for c in ["Recuperadosnovos", "emAcompanhamentoNovos", "codmun"] if c in df_final.columns]
df_final.drop(columns=cols_to_drop, inplace=True, errors="ignore")

# ==============================================================
# Incremental CSV saving with tqdm progress bar
# ==============================================================
chunk_size = 100_000
num_chunks = (len(df_final) // chunk_size) + 1
print("\nSaving consolidated dataset using tqdm...\n")
os.makedirs(os.path.dirname(output_csv), exist_ok=True)

with open(output_csv, "w", encoding="utf-8", newline="") as f:
    df_final.iloc[:0].to_csv(f, sep=";", index=False)
    for i in tqdm(range(num_chunks), desc="Saving chunks", unit="chunk"):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, len(df_final))
        df_final.iloc[start:end].to_csv(f, sep=";", index=False, header=False)

# ==============================================================
# Final summary
# ==============================================================
size_mb = os.path.getsize(output_csv) / 1024 / 1024
print(f"\n✅ Consolidated dataset successfully saved to: {output_csv}")
print(f"File size: {size_mb:.2f} MB")
print(f"Total rows: {len(df_final):,}".replace(",", "."))
print(f"Date range: {df_final['data'].min().date()} → {df_final['data'].max().date()}")
