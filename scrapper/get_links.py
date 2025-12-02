from bs4 import BeautifulSoup

input_html = "../receitaria.html"
output_txt = "../recipe_links.txt"
prefix = "https://www.receiteria.com.br/receita/"

# abre o arquivo HTML para leitura
with open(input_html, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# adiciona à lista apenas os links de receitas encontrados na página 
links_receitas = []
for tag in soup.find_all("a", href=True):
    href = tag["href"]
    if href.startswith(prefix):
        links_receitas.append(tag["href"])

# filtra os links duplicados ao criar um conjunto  
links_unicos = set(links_receitas)

# salva os links ao arquivo especificado 
with open(output_txt, "w", encoding="utf-8") as f:
    for link in links_unicos:
        f.write(link + "\n")
