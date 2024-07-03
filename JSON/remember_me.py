import json

def greet_user(filename):
    """Przywitanie użytkownika jego imieniem"""

    filename = 'imie.json'

    
    try:
        with open(filename) as f:               
            imie = json.load(f)

    except FileNotFoundError:
        imie = input("Podaj swoje imię: ")
        
        with open(filename,'w') as f:
            json.dump(f)
            print(f"Twoje imię zostało zapisane, {imie}!")

    else:
        print(f"Witaj ponownie, {imie}!")

greet_user('imie.json')