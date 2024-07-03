magicians = ['alicja', 'kuba', 'dawid']
for magician in magicians:  #pętla for umieszcza element listy w nowej zmiennej, używaj liczby pojedyńczej i mogiem podczas określania listy i jej składników
	print(f"Witaj magiku o imieniu {magician.title()}!")
	print(f"Nie możemy się doczekać twojej kolejnej sztuczki, {magician.title()}.\n")
print("Dziękujemy Wam za przybycie, drodzy magicy!")
pizze = ['margharita','peperoni','polo','salame']
for pizza in pizze:
	print(f"Moja ulubiona pizza to: {pizza.title()}")
print("Naprawdę lubię pizzę!!")

for value in range(1,6):  #range() to funkcja generująca liczby w podanym zakresie
	print(value)
numbers = list(range(6))  #funkcja range() może również utworzyć listę liczb
print(numbers)
even_numbers = list(range(0,11,2)) #trzeci argument funkcji range() reprezentuje o ile liczb zmienia się lista
print(even_numbers)
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
digits = list(range(1,10))
digits.append(0)
min(digits) #najmniejsza wartość listy
max(digits) #największa wartość listy
sum(digits) #suma elementów listy
squares = [value**2 for value in range(1,11)]  #[wyrażenie dla wartości, które mają zostać umieszczone na liście, dalej umieść pętlę odpowiedzialną za wygenerowanie liczb]
print(squares)
players = ['karol', 'martyna','michał', 'florian', 'ela',]
print(players[0:3])  #w ten sposób możemy pracować tylko na kawałku listy
print(players[:3])  #skoro nie został podany indeks początkowy, tworzenie wycinka python zaczął od początku listy
print(players[2:])  #teraz wyświetlone zostaną elementy od 3 do końca listy
print(players[-3:])  #funkcja zawsze będzie wyświetlała 3 elementy od końca
print("Oto trzech pierwszych graczy naszej drużyny: ")
for player in players[:3]:
	print(player.title())
#kopiowanie listy
my_foods = ['pizza', 'falafel', 'ciasto']
friend_foods = my_foods[:]
print(friend_foods)
#krotka - niemodyfikowalna lista
dimensions = [(200,50)]
print(dimensions[0])
my_t = (3,)  #definiując krotke jednoelementową i tak musimy dać przecinek po zmiennej
#nie można zmodyfikować krotki, ale można ją nadpisać
