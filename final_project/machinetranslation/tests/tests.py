import unittest
from translator import english_to_french, french_to_english

class Teste2f(unittest.TestCase):
    def teste2f(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Bonjour'),'Hello')
    
class Testf2e(unittest.TestCase):
    def testf2e(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Hello'),'Bonjour')

unittest.main()