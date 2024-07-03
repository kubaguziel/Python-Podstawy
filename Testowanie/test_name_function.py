import unittest

from name_function import formatted_name

class NamesTestCase(unittest.TestCase):
    """Testy dla programu name_function.py"""

    def test_first_last_name(self):
        """Czy dane w postaci 'Janis Joplin' są obsługiwane prawidłowo? """
        format_name = formatted_name('janis','joplin')
        self.assertEqual(format_name,'Janis Joplin')

if __name__ == '__main__':
    unittest.main()

    import unittest

from name_function import formatted_name

class NamesTestCase(unittest.TestCase):
    """Testy dla programu name_function.py"""

    def test_first_last_name(self):
        """Czy dane w postaci 'Janis Joplin' są obsługiwane prawidłowo? """
        format_name = formatted_name('janis','joplin')
        self.assertEqual(format_name,'Janis Joplin')

if __name__ == '__main__':
    unittest.main()

    
