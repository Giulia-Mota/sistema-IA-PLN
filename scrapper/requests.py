import os
import requests
import time

links_file = "../recipe_links.txt"       
output_dir = "../recipe_pages"
links_list = []

# cria a pasta caso ela ainda não exista
os.makedirs(output_dir, exist_ok=True)

# armazena cada link contido no arquivo em uma lista
with open(links_file, "r", encoding="utf-8") as f:
    links_list = [line.strip() for line in f if line.strip()]

# faz a requisição para cada link contido no arquivo 
for url in links_list:
    split = url.split("receita/")[1].split("/")[0]

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        file_path = os.path.join(output_dir, f"{split}.html")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"salvo: {file_path}")

        time.sleep(8)

    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
