from google import genai
from google.genai.types import Schema, Type
import json
import pandas as pd
from pandasgui import show

# LEIAM ANTES DE EXECUTAR #

# o Gemini tem um limite de 20 requisições por dia
# eu já gastei as minhas de hoje, vou testar amanhã para ver se consigo mais 
# antes de tudo, insiram a chave API de vocês
# para evitar confusões, separei de antemão as partes que cada um deve executar
# antes de executar, descomentem apenas o trecho de código com o nome de vocês
# os valores para as variáveis vão garantir que vocês processem os trechos certos do dataset
# cada execução gerará um arquivo JSON identificado pelo nome de vocês que depois juntaremos em um único arquivo

# ANDRÉ
#nome = "andre"
#start = 2000
#finish = 4000

# GABRIEL
#nome = "gabriel"
#start = 4000
#finish = 6000

# GIULIA
#nome = "giulia"
#start = 6000
#finish = 8000

# JOSÉ
#nome = "jose"
#start = 8000
#finish = 10000


try:
    client = genai.Client(api_key="")
except Exception as e:
    print(f"client error: {e}")
    exit()

instr = """

Você é um extrator de informações rigoroso e minimalista. 
Sua tarefa é analisar **UM ÚNICO** passo de uma receita e identificar apenas os utensílios, equipamentos e ferramentas de cozinha realmente necessários para realizar a ação daquele passo. 

**INSTRUÇÃO CRÍTICA DE ISOLAMENTO:** A análise deve ser feita estritamente sobre o texto do passo fornecido. Não utilize informações de passos anteriores, inferências de contexto geral da receita ou suposições sobre utensílios que possam ter sido mencionados antes. O contexto é **ZERO** fora do texto do passo atual.

Regras de Extração: 

1. Extraia somente utensílios/equipamentos estritamente necessários para executar o passo. Não extraia utensílios relacionados apenas à organização mental, mise en place ou separação de ingredientes sem uso direto. 
2. Extraia o nome mais específico que o contexto do **PASSO ATUAL** permitir. Por exemplo: “colher de pau” em vez de “colher”. 
3. Extraia utensílios/equipamentos implicitamente necessários para executar a ação. Por exemplo: “cozinhe” implica “panela” e “fogão”. Esta inferência deve ser feita **SOMENTE** com base na ação descrita no passo atual.
4. Quando houver alternativas (por exemplo, “multiprocessador ou liquidificador”), liste cada opção separadamente como itens distintos. 
5. Não extraia ingredientes, ações ou entidades abstratas. Extraia apenas objetos físicos utilizados no preparo. 
6. Classifique os utensílios e equipamentos extraídos de forma a permitir a contagem de itens explícitos e implícitos identificados. 

"""

output_schema = Schema(
    type=Type.ARRAY,
    description="Lista dos resultados de extração de utensílios para cada passo de receita.",
    items=Schema(
        type=Type.OBJECT,
        description="Resultado da análise de um único passo.",
        properties={
            "utensilios_equipamentos": Schema(
                type=Type.ARRAY,
                description="Lista de todos os utensílios e equipamentos identificados.",
                items=Schema(type=Type.STRING)
            ),
            "explicitos": Schema(
                type=Type.INTEGER,
                description="Contagem de utensílios e equipamentos explícitos."
            ),
            "implicitos": Schema(
                type=Type.INTEGER,
                description="Contagem de utensílios e equipamentos implícitos."
            )
        },
        required=["utensilios_equipamentos", "explicitos", "implicitos"]
    )
)

json_file = "../steps.json"
all_df = pd.read_json(json_file, orient="records", lines=True)
jump = 100

for first in range(start, finish, jump):
    last = first + jump
    few_df = all_df.iloc[first:last]
    dados_para_gemini = few_df.to_json(orient='records')

    try:
        chat = client.chats.create(
            model="gemini-2.5-flash",
            history=[
                {
                    "role": "user",
                    "parts": [{"text": instr}]
                }
            ],
            config={
                "response_mime_type": "application/json",
                "response_schema": output_schema
            }
        )

        resp = chat.send_message(dados_para_gemini)


        data_analyzed = json.loads(resp.text)
        gemini_df = pd.DataFrame(data_analyzed)
        gemini_df.to_json(f"../parte_{nome}.json", orient="records", lines=True, force_ascii=False, mode="a")

    
    except Exception as e:
        print(e)
        break

