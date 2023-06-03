import unittest
from translator import english_to_french, french_to_english
class TranslationTests(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertEqual(english_to_french("thank you"), "merci")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("bonjour"), "hello")
        self.assertEqual(french_to_english("merci"), "Thank you")

if __name__ == '__main__':
    unittest.main()