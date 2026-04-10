import requests
import pandas as pd

url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Erro ao acessar o site:", response.status_code)
    exit()

# Usa pandas lendo o HTML já carregado (evita bloqueio)
tables = pd.read_html(response.text)

df = tables[0]

df = df[["Player", "Squad", "Sh", "SoT"]]

df.columns = ["Jogador", "Time", "Chutes", "Chutes no Gol"]

df.to_csv("dados_jogadores.csv", index=False)

print("Dados coletados com sucesso!")
