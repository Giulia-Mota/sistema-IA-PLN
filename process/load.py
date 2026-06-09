import pandas as pd
from pandasgui import show

dataset = "C:/Users/jujum/OneDrive/Documents/Receitas IA/receitas-PLN/merged_parte_gabriel.json"
df = pd.read_json(dataset, orient="records", lines=True)
show(df)

