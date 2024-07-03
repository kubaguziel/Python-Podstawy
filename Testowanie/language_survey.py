from survey import AnonymousSurvey

#Zdefiniowanie pytania i utworzenie ankiety

question = "Jaki jest twój ojczysty język?"

my_survey = AnonymousSurvey(question)

#wyświetlenie pytania i przechowywanie odpowiedzi na nie
my_survey.show_questions()
print("Wpisz 'q', aby zakończyć działanie programu. \n")

while True:
    response = input("Język: ")
    if response == 'q':
        break

    my_survey.store_response(response)

#Wyświetlanie wyników ankiety
print("\nDziękujemy wszystkim za wzięcie udziału w ankiecie.")
my_survey.show_results()