from solution import most_frequent_character
### test cases
import unittest

class TestMostFrequentCharacter(unittest.TestCase):
    def test_single_character(self):
        # Test a string with only one character
        self.assertEqual(most_frequent_character("a"), "a")
    
    def test_equal_frequencies(self):
        # Test a string where all characters have the same frequency
        self.assertEqual(most_frequent_character("abcABC"), "a")
    
    def test_mixed_case(self):
        # Test a string with mixed case letters
        self.assertEqual(most_frequent_character("Hello World!"), "l")
    
    def test_special_characters(self):
        # Test a string with special characters
        self.assertEqual(most_frequent_character("!@#$%^&*()_+"), "!")
    
    def test_numbers_and_symbols(self):
        # Test a string with numbers and symbols
        self.assertEqual(most_frequent_character("1234567890!@#$%^&*()_+"), "1")
    
    def test_empty_string(self):
        # Test an empty string
        self.assertEqual(most_frequent_character(""), "")
    
    def test_large_input(self):
        # Test a large input string
        large_input = "a" * 1000000 + "b" * 999999
        self.assertEqual(most_frequent_character(large_input), "a")  # Modified output
    
    def test_multiple_most_frequent(self):
        # Test a string with multiple characters having the same highest frequency
        self.assertEqual(most_frequent_character("abca"), "a")

if __name__ == '__main__':
    unittest.main()
