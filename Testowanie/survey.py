class AnonymousSurvey():
    """Przechowuje anonimowe odpowiedzi na pytania w ankiecie."""
    def __init__(self,question) -> None:
        """Przechowuje pytanie i przygotowuje do przechwytywania odpowiedzi"""
        self.question = question
        self.responses = []

    def show_questions(self):
        """Wyświetla pytanie z ankiety"""
        print(self.question)

    def store_response(self, new_response):
        """Przechowuje pojedyńczą odpowiedź na pytanie z ankiety"""
        self.responses.append(new_response)

    def show_results(self):
        """Wyświetla wszystkie udzielone odpowiedzi"""
        print("Oto wyniki twojej ankiety.")
        for response in self.responses:
            print(f"- {response}")