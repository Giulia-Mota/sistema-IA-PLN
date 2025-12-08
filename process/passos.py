import pandas as pd

dataset = "../recipes.json"
df = pd.read_json(dataset, orient="records", lines=True)
steps_list = []

def construir_json_minimalista():    
    global df, steps_list

    for recipe_index, row in df.iterrows():
        instructions = row['recipeInstructions']
        
        for step in instructions:
            step_obj = {
                "passo": step, 
                "receita": recipe_index, 
            }
            
            steps_list.append(step_obj)
            
construir_json_minimalista()

steps = pd.DataFrame(steps_list)
steps.to_json("../steps.json", orient="records", lines=True, force_ascii=False, mode="a")
