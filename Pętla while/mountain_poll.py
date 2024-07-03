responses = {}

#ustawienie flagi pokazującej czy ankieta jest aktywna
active = True
while active:
    #pytanie o imie i odpowiedz uczestnika ankiety
    name = input("\nJak masz na imię? ")
    answer = input("\nNa który szczyt chciałbyś się wspiąć pewnego dnia? ")

    #umieszczenie odpowiedzi w słowniku
    responses[name] = answer

    #ustalenie czy ktokolwiek jeszcze chce wziąć udział w ankiecie
    repeat = input("Czy ktoś jeszcze chciałby wziąć udział w ankiecie? (tak / nie): ")
    if repeat == 'nie':
         active = False

print("\n---Wynik ankiety---")
for name,answer in responses.items():
     print(f"\n{name} chciałby wspiąć się na {answer.title()}.")