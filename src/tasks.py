import pandas as pd
import requests
from datetime import datetime
from ...models import CovidRecord

def fetch_covid_data_sp():
    """Baixa dados da API Brasil.IO e atualiza o banco"""
    TOKEN = "SEU_TOKEN_AQUI"
    headers = {"Authorization": f"Token {TOKEN}"}
    url = "https://brasil.io/api/dataset/covid19/caso_full/data/"
    params = {"state": "SP", "city": "São Paulo", "page_size": 10000}

    rows = []
    while url:
        r = requests.get(url, headers=headers, params=params)
        data = r.json()
        rows.extend(data["results"])
        url = data["next"]
        params = None

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["date"] >= "2021-01-01"]

    # calcular campos derivados
    df = df.sort_values("date")
    df["new_cases"] = df["confirmed"].diff().fillna(0).astype(int)
    df["new_deaths"] = df["deaths"].diff().fillna(0).astype(int)

    # salvar no banco
    CovidRecord.objects.all().delete()
    for _, row in df.iterrows():
        CovidRecord.objects.create(
            date=row["date"].date(),
            confirmed=int(row["confirmed"]),
            deaths=int(row["deaths"]),
            new_cases=int(row["new_cases"]),
            new_deaths=int(row["new_deaths"]),
        )

    print(f"✅ {len(df)} registros atualizados.")
