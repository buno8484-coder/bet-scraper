import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Erro ao acessar o site")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")

if not tables:
    print("Nenhuma tabela encontrada")
    exit()

table = tables[0]

players = []
rows = table.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    
    if len(cols) > 18:
        player = cols[0].text.strip()
        team = cols[2].text.strip()
        shots = cols[17].text.strip()
        shots_on_target = cols[18].text.strip()

        players.append({
            "Jogador": player,
            "Time": team,
            "Chutes": shots,
            "Chutes no Gol": shots_on_target
        })

df = pd.DataFrame(players)

if df.empty:
    print("Tabela vazia")
else:
    df.to_csv("dados_jogadores.csv", index=False)
    print("Dados coletados com sucesso!")
