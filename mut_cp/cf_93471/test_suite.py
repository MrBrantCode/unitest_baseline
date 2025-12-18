from solution import reverse_string_ignore_whitespace
### test cases
import unittest

class TestReverseStringIgnoreWhitespace(unittest.TestCase):
    """
    This class contains unit tests for the reverse_string_ignore_whitespace function.
    """

    def test_empty_string(self):
        """
        Test with an empty string input.
        Expected output: ''
        """
        self.assertEqual(reverse_string_ignore_whitespace(""), "")

    def test_single_character(self):
        """
        Test with a single character input.
        Expected output: the same character (lowercase).
        """
        self.assertEqual(reverse_string_ignore_whitespace("A"), "a")

    def test_with_whitespace(self):
        """
        Test with a string containing leading and trailing whitespace.
        Expected output: reversed string without whitespace.
        """
        self.assertEqual(reverse_string_ignore_whitespace(" Hello World "), "dlrowolleh")

    def test_with_special_characters(self):
        """
        Test with a string containing special characters.
        Expected output: reversed string without whitespace, special characters are preserved.
        """
        self.assertEqual(reverse_string_ignore_whitespace("Hello!@# World$%^"), "^%$wodllrlo!@#olleh")

    def test_with_numbers(self):
        """
        Test with a string containing numbers.
        Expected output: reversed string without whitespace, numbers are preserved.
        """
        self.assertEqual(reverse_string_ignore_whitespace("123 Hello 456 World"), "dlrowolleh654321")

    def test_mixed_case(self):
        """
        Test with a string containing mixed case letters.
        Expected output: reversed string in lowercase.
        """
        self.assertEqual(reverse_string_ignore_whitespace("HeLlO WoRlD"), "dlrowolleh")  # Modified output

if __name__ == '__main__':
    unittest.main()
