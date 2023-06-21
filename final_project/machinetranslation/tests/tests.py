import unittest
from translator import english_to_french, french_to_english

class test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"), "bonjour")

    def test2(self):
        self.assertEqual(english_to_french("bonjour"), "hello")

class test_frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("hello"), "bonjour")

    def test2(self):
        self.assertEqual(french_to_english("bonjour"), "hello")
unittest.main()                      