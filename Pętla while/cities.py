message = "\nPodaj nazwy miast, które chciałbyś odwiedzić: "
message += "\n(Gdy zakończysz podawanie miast, napisz 'koniec'.) "

while True:
    city = input(message)
    if city == 'koniec':
        break
    else:
        print(f"Chciałbym odwiedzić {city.title()}! ")

