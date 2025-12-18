from solution import longest_substring_length
### test cases
import unittest

class TestLongestSubstringLength(unittest.TestCase):
    def test_empty_string(self):
        # Test case for an empty string
        self.assertEqual(longest_substring_length(""), 0)

    def test_single_character(self):
        # Test case for a single character string
        self.assertEqual(longest_substring_length("a"), 1)

    def test_no_repeated_characters(self):
        # Test case for a string with no repeated characters
        self.assertEqual(longest_substring_length("abcde"), 5)

    def test_with_repeated_characters(self):
        # Test case for a string with repeated characters
        self.assertEqual(longest_substring_length("abca"), 3)

    def test_mixed_case(self):
        # Test case for a string with mixed case letters
        self.assertEqual(longest_substring_length("AbCaBc"), 6)

    def test_special_characters(self):
        # Test case for a string with special characters
        self.assertEqual(longest_substring_length("!@#$%^&*()"), 10)

    def test_long_string(self):
        # Test case for a longer string with repeated characters
        self.assertEqual(longest_substring_length("pwwkew"), 3)  # "wke" or "kew" is the longest substring with no repeated characters

    def test_all_same_characters(self):
        # Test case for a string with all the same characters
        self.assertEqual(longest_substring_length("aaaaa"), 1)  # The longest substring with no repeated characters is "a" (length 1)  # Modified output

    def test_complex_string(self):
        # Test case for a complex string with various characters
        self.assertEqual(longest_substring_length("dvdf"), 3)  # "vdf" is the longest substring with no repeated characters

if __name__ == '__main__':
    unittest.main()
