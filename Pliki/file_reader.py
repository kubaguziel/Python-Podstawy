filePath = 'A:\programowanie\python\Pliki\pi_million_digits.txt'

with open(filePath) as file_object:
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines() #metoda readlines pobiera jeden wiersz z pliku

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Podaj datę swoich urodzin w formacie ddmmrr: ")
if birthday in pi_string:
    print("Twoja data urodzenia znajduje się wśród miliona pierwszych cyfr liczby pi!!!")
else:
    print("Twojej daty urodzenia nie ma wśród pierwszego miliona cyfr liczby pi:(") 
