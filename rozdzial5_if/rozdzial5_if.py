cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())


requested_topping = 'pieczarki'
if requested_topping!='anchois':
    print("Proszę o anchois!")


    age = 18
    if age < 18:
        print("Osoba niepełnoletnia!")
    else:
        print("Osoba pełnoletnia:)")

age1 = 20
age2 = 17

if age1>18 and age2>18:                         #operator and
    print("Obie osoby mogą wejść.")
if age1>18 and age2<18:
    print("Tylko pierwsza osoba może wejść.")
if age1<18 and age2<18:
    print("Nikt nie może wejść.")

if age1==20 or age2==20:                        #operator or
    print("Jedna z osób ma 20 lat.")

requested_toppings = ['pieczarki','cebula']
'pieczarki' in requested_toppings                #sprawdzenie czy dana wartość istnieje na liście
'pepperoni' in requested_toppings

if 'ananas' not in requested_toppings:           #sprawdzenie czy dany element nie pojawia się na liście
    print("Możesz jeść w tej pizzerii.")

