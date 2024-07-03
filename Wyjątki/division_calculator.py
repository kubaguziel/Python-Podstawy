# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Nie można dzielić przez zero!")

print("Podaj dwie liczby, które zostaną przez siebie podzielone: ")
print("Wciśnij q, by zakończyć działanie programu. ")
while True:
    first_number = input("\nPierwsza liczba: ")
    if first_number == 'q':
        break
    second_number = input("\nDruga liczba: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero!!!")
    else:
        print(answer)
