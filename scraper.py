import pandas as pd

url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"

tables = pd.read_html(url)

df = tables[0]

df = df[["Player", "Squad", "Sh", "SoT"]]

df.columns = ["Jogador", "Time", "Chutes", "Chutes no Gol"]

df.to_csv("dados_jogadores.csv", index=False)

print("Dados coletados com sucesso!")
