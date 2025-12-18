from solution import count_vowels
### test cases
import unittest

class TestCountVowels(unittest.TestCase):
    """
    Test class for the count_vowels function.
    """

    def test_empty_string(self):
        """
        Test with an empty string.
        Expected result: 0
        """
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        """
        Test with a string containing no vowels.
        Expected result: 0
        """
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_only_vowels(self):
        """
        Test with a string containing only vowels.
        Expected result: Length of the string
        """
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_mixed_characters(self):
        """
        Test with a string containing a mix of letters, numbers, and special characters.
        Expected result: Number of vowels in the string
        """
        self.assertEqual(count_vowels("Hello, World! 123"), 3)

    def test_case_insensitivity(self):
        """
        Test with a string containing both uppercase and lowercase vowels.
        Expected result: Correct count of vowels regardless of case
        """
        self.assertEqual(count_vowels("HeLlO WoRlD"), 3)  # Modified output

    def test_special_characters(self):
        """
        Test with a string containing special characters.
        Expected result: Correct count of vowels, ignoring special characters
        """
        self.assertEqual(count_vowels("!@#$%^&*()_+"), 0)  # Modified output

if __name__ == '__main__':
    unittest.main()
