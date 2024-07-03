first_name = "Kuba"
second_name = "Guziel"
full_name = f"{first_name} {second_name}"
print(f"Witaj, {full_name.title()}!") #.title zmienia pierwsza litere imienia i nazwiska na dużą
print(full_name)
print("\tKuba Guziel")
print("Języki: \nPython\nJava\nC++")
print("Języki: \n\tPython\n\tJava\n\tC++")
favorite_language = "python "
print(favorite_language.rstrip()) #.rstrip() usuwa białe znaki z prawej strony wyrazu tymczasowo
favorite_language = favorite_language.rstrip() #usuwa biały znak permanentnie
#strip usuwa białe znoki z obu stron wyrazu, lstrip z lewej strony
imie = "eryk"
print(f"Witaj {imie.title()}! Czy chcesz dziś poznać Pythona?")
print(imie.lower()) #.lower() zamienia znaki na małe litery
print(imie.upper()) #.upper() zamienia znaki na duże litery
print('Albert Einstein powiedział kiedyś: "Osoba, która nie popełniła błędu, jest kimś, kto nigdy nie próbował niczego nowego."')
wynik = 3**2 #3 do potęgi 2
print(wynik)
1000000 == 1_000_000 #cyfry można grupować za pomocą znaków podkreślenia, aby polepszyć czytelność kodu
x, y, z = 0, 0, 0 #można przypisać kilka zmiennych jednocześnie
LICZBA_PI=3.14 #do oznaczania stałych używa się wielkich liter
#import this <- zbiór zasad Zen P
