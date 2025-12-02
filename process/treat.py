import os
from bs4 import BeautifulSoup
import json
import pandas as pd
from pandasgui import show

input_dir = "../recipe_pages/"

files = os.listdir(input_dir)

all = []

def filtrar_receita(data):
    simples = [
        "name",
        "url",
        "totalTime",
        "prepTime",
        "cookTime",
        "recipeYield",
        "recipeCategory",
        "recipeCuisine"
    ]
    
    filtrado = {}

    for chave in simples:
        filtrado[chave] = data.get(chave)

    rating = data.get("aggregateRating")
    if rating:
        filtrado["ratingValue"] = rating.get("ratingValue")
        filtrado["bestRating"]  = rating.get("bestRating")
        filtrado["ratingCount"] = rating.get("ratingCount")
    else:
        filtrado["ratingValue"] = None
        filtrado["bestRating"]  = None
        filtrado["ratingCount"] = None

    filtrado["recipeIngredient"] = data.get("recipeIngredient", [])

    passos = data.get("recipeInstructions", [])
    filtrado["recipeInstructions"] = [
        passo.get("text", "").strip()
        for passo in passos
        if isinstance(passo, dict)
    ]

    return filtrado


for i, file in enumerate(files):
    file_path = os.path.join(input_dir, file)

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    scripts = soup.find_all("script", {"type": "application/ld+json"})
    
    for script in scripts:
        try:
            page_data = json.loads(script.string)
            if page_data.get("@type") == "Recipe":
                filtered = filtrar_receita(page_data)
                all.append(filtered)
                break
        except Exception:
            continue

    print(f"[{i}]: {file_path}")
    
    if i % 50 == 0:
        print(f"processed: {i}/{len(files)}")


df = pd.DataFrame(all)
df.to_json("../dataset.json", orient="records", lines=True, force_ascii=False, mode="a")
show(df)
