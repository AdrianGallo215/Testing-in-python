import json
import os

FILE_PATH = 'etiquetas.json'

def load_tags():
    if(os.path.exists(FILE_PATH)):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
        
    return ["general", "trabajo", "universidad", "personal"]
    
def save_tag(tags):
    with open(FILE_PATH, "w") as file:
        json.dump(tags, file)

def add_tag(newTag):
    tags = load_tags()

    if newTag not in tags:
        tags.append(newTag)
        save_tag(tags)

