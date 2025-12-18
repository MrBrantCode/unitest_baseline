from solution import format_sentence
### test cases
import unittest

class TestFormatSentence(unittest.TestCase):
    def test_no_vowels(self):
        # Test case where all strings do not contain vowels
        self.assertEqual(format_sentence(["bcdfg", "pqrst", "xyz"]), "bcdfg pqrst xyz")

    def test_with_vowels(self):
        # Test case where some strings contain vowels
        self.assertEqual(format_sentence(["hello", "world", "python", "is", "fun"]), "")

    def test_mixed_case(self):
        # Test case with mixed case strings
        self.assertEqual(format_sentence(["Hello", "WORLD", "Python", "Is", "Fun"]), "world")

    def test_empty_list(self):
        # Test case with an empty list
        self.assertEqual(format_sentence([]), "")

    def test_single_string(self):
        # Test case with a single string
        self.assertEqual(format_sentence(["test"]), "")  # Modified output

    def test_alternating_case(self):
        # Test case to ensure correct alternating case
        self.assertEqual(format_sentence(["abc", "DEF", "ghi", "JKL", "mno", "PQR"]), "abc def ghi jkl mno pqr")  # Modified output

if __name__ == '__main__':
    unittest.main()
