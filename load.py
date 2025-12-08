import pandas as pd
from pandasgui import show

dataset = "../gemini.json"
df = pd.read_json(dataset, orient="records", lines=True)
show(df)

