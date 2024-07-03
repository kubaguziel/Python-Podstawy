def formatted_name(imie,nazwisko):
    """Zwraca elegancko sformatowane imie i nazwisko"""
    full_name=f"{imie.title()} {nazwisko.title()}"
    return full_name

while True:
    print("Proszę podać imię i nazwisko: ")
    print("Naciśnij q, aby zakończyć działanie programu.")
    f_name = input("Imię: ")
    if f_name == 'q':
        break
    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break 


    sformatowane = formatted_name(f_name,l_name)
    print(f"\nWitaj, {sformatowane}!")