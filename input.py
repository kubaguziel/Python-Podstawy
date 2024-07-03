message = input("Powiedz coś o sobie, a wyświetlę to na ekranie: ")
print(message)

name = input("Podaj swoje imię: ")
print(f"Witaj, {name}!")

# #komunikaty mające więcej niż jedną linijkę

komunikat = "Jeżeli powiesz nam coś o sobie, będziemy mogli przygotować spersonalizowany komunikat."
komunikat += "\nJak masz na imię? "

name = input(komunikat)
print(f"Witaj, {name}!")

#wszystkie dane wejściowe python interpretuje jako ciąg tekstowy, więc jeśli chcemy dostać np. liczbę, to musimy ją przekonwertować

age = input("Ile masz lat? ")
age = int(age)
if age >= 18:
    print("Możesz wejść")
else: print("Nie możesz wejść")

#sprawdzenie czy liczba jest parzysta czy nie

number = input("Podaj liczbę, aby dowiedzieć się, czy jest parzysta czy nieparzysta: ")
number = int(number)
if number % 2 == 0:
    print(f"\nLiczba {number} jest parzysta.")
else: print(f"\nLiczba {number} jest nieparzysta.")

