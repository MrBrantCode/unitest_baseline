from solution import entrance
### test cases
import unittest

class TestEntranceFunction(unittest.TestCase):
    def test_palindrome_even_chars(self):
        # Test case where the input string is a palindrome and all characters occur even times.
        result = entrance("A man a plan a canal Panama")
        self.assertIn("even times", result)  # Check if the result contains the phrase 'even times'
        self.assertIn("{'a': 10, 'n': 4, 'm': 2, 'p': 2, 'l': 2, 'c': 2, ' ': 6}", result)  # Check the character count dictionary

    def test_palindrome_odd_chars(self):
        # Test case where the input string is a palindrome but not all characters occur even times.
        result = entrance("Madam Arora teaches malayalam")
        self.assertIn("not a palindrome", result)  # Check if the result contains the phrase 'not a palindrome'

    def test_non_palindrome(self):
        # Test case where the input string is not a palindrome.
        result = entrance("Hello World")
        self.assertIn("not a palindrome", result)  # Check if the result contains the phrase 'not a palindrome'

    def test_empty_string(self):
        # Test case where the input string is empty.
        result = entrance("")
        self.assertEqual(result, "The string is a palindrome and all characters occur even times: {}")  # Check if the result is correct for an empty string

    def test_single_char(self):
        # Test case where the input string is a single character.
        result = entrance("a")
        self.assertEqual(result, "The string is a palindrome and all characters occur even times: {'a': 1}")  # Check if the result is correct for a single character

    def test_special_characters(self):
        # Test case where the input string contains special characters.
        result = entrance("Was it a car or a cat I saw?")
        self.assertIn("even times", result)  # Check if the result contains the phrase 'even times'
        self.assertIn("{'w': 3, 's': 3, 'i': 3, 't': 3, 'a': 4, 'c': 2, 'r': 2, 'o': 2, ' ': 7, '?': 1}", result)  # Check the character count dictionary

if __name__ == '__main__':
    unittest.main()
