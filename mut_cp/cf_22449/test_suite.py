from solution import replace_vowels
### test cases
import unittest

class TestReplaceVowels(unittest.TestCase):
    def test_no_vowels(self):
        # Test when the input string has no vowels.
        self.assertEqual(replace_vowels("bcdfg"), "bcdfg")

    def test_all_vowels(self):
        # Test when the input string consists entirely of vowels.
        self.assertEqual(replace_vowels("aeiouAEIOU"), "_")

    def test_mixed_case(self):
        # Test when the input string has both uppercase and lowercase vowels.
        self.assertEqual(replace_vowels("aEiOuAeIoU"), "_")

    def test_consecutive_vowels(self):
        # Test when the input string has consecutive vowels.
        self.assertEqual(replace_vowels("aaeeiiou"), "_")

    def test_punctuation_marks(self):
        # Test when the input string contains punctuation marks.
        self.assertEqual(replace_vowels("a,e.i:o.u!"), "_")

    def test_mixed_content(self):
        # Test when the input string contains a mix of letters and punctuation marks.
        self.assertEqual(replace_vowels("Hello, World!"), "H_ll_, W_rld!")  # Modified output

    def test_empty_string(self):
        # Test when the input string is empty.
        self.assertEqual(replace_vowels(""), "")  # Modified output

if __name__ == '__main__':
    unittest.main()
