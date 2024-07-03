def greet_user(username):
    """Wyświetla proste powitanie.""" #ten komentarz to tak zwany docstring czyli opis działania funkcji, który potem znajdzie się w dokumentacji
    print(f"\nWitaj, {username.title()}! ")

    
imie = input("Jak masz na imię? ")
greet_user(imie)
