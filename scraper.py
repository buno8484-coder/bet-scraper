import requests
import pandas as pd

url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

try:
    tables = pd.read_html(response.text)
    df = tables[0]

    df = df[["Player", "Squad", "Sh", "SoT"]]
    df.columns = ["Jogador", "Time", "Chutes", "Chutes no Gol"]

except:
    print("Erro ao pegar dados, criando CSV vazio")
    df = pd.DataFrame(columns=["Jogador", "Time", "Chutes", "Chutes no Gol"])

# SEMPRE cria o arquivo
df.to_csv("dados_jogadores.csv", index=False)

print("CSV criado com sucesso!")
