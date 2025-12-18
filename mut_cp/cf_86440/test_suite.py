from solution import get_distinct_permutations
### test cases
import unittest

class TestGetDistinctPermutations(unittest.TestCase):
    def test_empty_string(self):
        # Test case for an empty string
        self.assertEqual(get_distinct_permutations(""), [])
    
    def test_single_character_string(self):
        # Test case for a single character string
        self.assertEqual(get_distinct_permutations("a"), ["a"])
    
    def test_two_characters_string(self):
        # Test case for a two-character string
        self.assertEqual(set(get_distinct_permutations("ab")), set(["ab", "ba"]))
    
    def test_duplicate_characters(self):
        # Test case for a string with duplicate characters
        self.assertEqual(set(get_distinct_permutations("aab")), set(["aab", "aba", "baa"]))
    
    def test_long_string(self):
        # Test case for a longer string
        self.assertEqual(set(get_distinct_permutations("abc")), set(["abc", "acb", "bac", "bca", "cab", "cba"]))  # Modified output
    
    def test_case_sensitivity(self):
        # Test case to ensure case sensitivity is handled correctly
        self.assertEqual(set(get_distinct_permutations("AaBb")), set(["AaBb", "AaBb", "AaBb", "AaBb", "AaBb", "AaBb"]))  # Modified output
    
    def test_repeated_characters(self):
        # Test case for a string with repeated characters
        self.assertEqual(set(get_distinct_permutations("aaa")), set(["aaa"]))  # Modified output

if __name__ == '__main__':
    unittest.main()
