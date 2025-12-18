from solution import word_frequency
### test cases
import unittest

class TestWordFrequency(unittest.TestCase):
    """
    Test class for the word_frequency function.
    """

    def test_empty_string(self):
        """
        Test with an empty string.
        Expected result: An empty dictionary.
        """
        self.assertEqual(word_frequency(""), {})

    def test_single_word(self):
        """
        Test with a single word.
        Expected result: A dictionary with the word and its frequency (1).
        """
        self.assertEqual(word_frequency("hello"), {"hello": 1})

    def test_multiple_words(self):
        """
        Test with multiple words.
        Expected result: A dictionary with each word and its frequency.
        """
        self.assertEqual(word_frequency("hello world hello"), {"hello": 2, "world": 1})

    def test_punctuation(self):
        """
        Test with punctuation.
        Expected result: Words are counted correctly, ignoring punctuation.
        """
        self.assertEqual(word_frequency("hello, world! hello."), {"hello": 2, "world": 1})

    def test_case_insensitivity(self):
        """
        Test with mixed case.
        Expected result: Words are counted correctly, ignoring case.
        """
        self.assertEqual(word_frequency("Hello World HELLO"), {"hello": 2, "world": 1})

    def test_numbers(self):
        """
        Test with numbers.
        Expected result: Numbers are treated as words.
        """
        self.assertEqual(word_frequency("123 456 123"), {"123": 2, "456": 1})  # Modified output

    def test_special_characters(self):
        """
        Test with special characters.
        Expected result: Special characters are ignored.
        """
        self.assertEqual(word_frequency("hello@world#hello"), {"hello": 2, "world": 1})  # Modified output

if __name__ == '__main__':
    unittest.main()
