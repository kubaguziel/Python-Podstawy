for value in range(1,21):
    print(value)
odliczanie = [value for value in range(1,10**6+1)]
print(min(odliczanie))
print(max(odliczanie))
print(sum(odliczanie))
lista = [value for value in range(1,20,2)]
print(lista)

lista2 = [value**3 for value in range(3,30)]

#for liczba in lista2:
    #print(liczba)


szesciany = []

for value in range(1,11):
   print(value)
   szesciany.append(value**3)

print(f"To sześciany 10 liczb początkowych: {szesciany}")

