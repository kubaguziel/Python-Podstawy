def describe_pet(animal_type, name):
    """Wyświetla informację o zwierzęciu"""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"\nMa na imię {name.title()}.")

describe_pet('pies', 'dafik')
describe_pet("kot","ada") #bez znaczenia czy ' ' czy " "