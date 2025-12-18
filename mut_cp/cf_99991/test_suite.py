from solution import remove_word
This function uses regular expressions to replace the word with an empty string, ignoring case and special characters.

### test cases
import unittest

class TestRemoveWordFunction(unittest.TestCase):
    def test_remove_single_word(self):
        # Test removing a single word from a sentence
        self.assertEqual(remove_word("Hello World", "world"), "Hello ")
        
    def test_remove_phrase(self):
        # Test removing a phrase from a sentence
        self.assertEqual(remove_word("Good morning everyone", "morning"), "Good  everyone")
        
    def test_case_insensitivity(self):
        # Test if the function is case-insensitive
        self.assertEqual(remove_word("Good Morning Everyone", "mORNING"), "Good  Everyone")
        
    def test_special_characters(self):
        # Test if the function ignores special characters
        self.assertEqual(remove_word("Good! Morning? Everyone.", "morning"), "Good! ? Everyone.")
        
    def test_empty_text(self):
        # Test if the function handles an empty text input
        self.assertEqual(remove_word("", "test"), "")
        
    def test_empty_word(self):
        # Test if the function handles an empty word input
        self.assertEqual(remove_word("Hello World", ""), "Hello World")
        
    def test_word_not_in_text(self):
        # Test if the function returns the original text when the word is not in the text
        self.assertEqual(remove_word("Hello World", "test"), "Hello World")  # Modified output

# To run the tests, you would typically use a command like:
# python -m unittest TestRemoveWordFunction
# However, for demonstration purposes, we will not execute the tests here.

if __name__ == '__main__':
    unittest.main()
