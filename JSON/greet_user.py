import json

filename = 'imie.json'

with open(filename) as f:
    imie = json.load(f)
    print(f"Witaj ponownie, {imie}!")