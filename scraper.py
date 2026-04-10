import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

players = []
rows = table.find_all("tr")[1:]

for row in rows:
    cols = row.find_all("td")
    if len(cols) > 0:
        try:
            player = cols[0].text
            team = cols[2].text
            shots = cols[17].text
            shots_on_target = cols[18].text

            players.append({
                "Jogador": player,
                "Time": team,
                "Chutes": shots,
                "Chutes no Gol": shots_on_target
            })
        except:
            pass

df = pd.DataFrame(players)

df.to_csv("dados_jogadores.csv", index=False)

print("Dados coletados com sucesso!")
