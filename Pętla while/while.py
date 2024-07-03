#składnia pętli while

current_number = 1
while current_number <=10:
    print(current_number)
    current_number += 1

komunikat = "\nNapisz coś o sobie, a wyświetlę to na ekranie: "
komunikat += "\nNapisz 'koniec', aby zakończyć działanie programu. "
message = ""
while message != "koniec":
    message = input(komunikat)
    if message != "koniec":
        print(message)


# gdy chcemy, aby program miał kilka warunków, dla których może przestać działać, możemy dodać flagę

komunikat = "\nNapisz coś o sobie, a wyświetlę to na ekranie. "
komunikat += "\nNapisz 'koniec', aby zakończyć działanie programu: "
message = ""

active = True

while active:
    message = input(komunikat)
    if message == "koniec":
        active = False
    else:    
        print(message)

