import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testy dla klasy AnonymousSurvey"""
    def setUp(self):
        """Utworzenie ankiety i zestawu odpowiedzi do użycia we wszystkich metodach testowych"""
        question = "Jaki jest twój język ojczysty? "
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['polski','angielski','włoski']
    

    def test_store_single_response(self):
        """Sprawdzenie, czy pojedyńcza odpowiedź jest prawidłowo przechowywana."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    
    def test_store_three_responses(self):
        """Sprawdzenie czy 3 ostatnie odpowiedzi są dobrze przechowywane."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)



if __name__ == '__main__':
    unittest.main()