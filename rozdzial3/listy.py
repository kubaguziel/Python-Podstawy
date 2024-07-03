#listy
imiona = ['Kuba','Natalia', 'Barbara', 'Tomasz']
print(imiona)
#odwołanie do konkretnego elementu listy (jak w tabeli c++)
print(imiona[0]) #wartość zwracana bez nawiasów i apostrofów
print(imiona[-1]) #indeks -1 zwraca ostatni element listy, indeks -2 zwraca 2 od końca element listy
message = f"Mój tata to {imiona[-1].title()}"
print(message)
motorcycles = ['honda','yamaha','kawasaki','suzuki']
print(motorcycles)
motorcycles[-1] = 'ducati' #możemy modyfikować elementy listy
print(motorcycles)
motorcycles.append('suzuki') #funkcja dodająca nowy element na końcu listy
print(motorcycles)
motorcycles.insert(0,'BMW') #funkcja dodaje element na indeks 0, a reszte przesuwa o 1
print(motorcycles)
del motorcycles[1] #funkcja usuwa element na podstawie jego położenia
print(motorcycles)
popped_motorcycle = motorcycles.pop() #funkcja usuwa ostatni element listy, ale pozwala na dalszą pracę z nim
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(1) #funkcja pozwala także na usunięcie elementu o danym indeksie
print(first_owned)
motorcycles = ['honda','yamaha','kawasaki','suzuki']
print(f"Moje motocykle to: {motorcycles}")
motorcycles.remove('honda') #funkcja usuwa element o danej wartości (usuwa tylko 1 wystąpoienie tego elementu na liście)
print(f"Moje motocykle to: {motorcycles}")
auta = ['bmw','toyota','mclaren','audi']
auta.sort() #funkcja sortuje liste w kolejnosci alfabetycznej, trwale zmienia kolejność elementów na liście
print(auta)
auta.sort(reverse=True) #funkcja sortuje liste w odwrotnej kolejności
print(auta)
auta = ['bmw','toyota','mclaren','audi']
print(f"Oto lista początkowa: {auta}")
print(f"\nOto lista posortowana: {sorted(auta)}") #funkcja wyświetla posortowaną listę, ale nie zmienia kolejności elementów na liście; również akceptuje argument reverse=True
auta.reverse() #funkcja odwraca kolejność elementów na liście
print(auta)
len(auta) #funkcja zwraca ilość elementów listy (elementy są liczone od 1 nie od 0)
