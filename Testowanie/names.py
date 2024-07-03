from name_function import formatted_name

print("Wpisz q, aby zakończyć działanie programu")

while True:
    first = input("Podaj imię: ")
    if first == 'q':
        break

    last = input("Podaj swoje nazwisko: ")
    if last == 'q':
        break

    sformatowane = formatted_name(first,last)
    print(f"Elegancko sformatowane imię: {sformatowane}")