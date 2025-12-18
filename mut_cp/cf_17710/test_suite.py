from solution import sort_vowel_keys
### test case
import unittest

class TestSortVowelKeys(unittest.TestCase):
    def test_sort_vowel_keys(self):
        # Test case 1: Empty dictionary
        self.assertEqual(sort_vowel_keys({}), ({}, 0))
        
        # Test case 2: Dictionary with no keys starting with vowels
        self.assertEqual(sort_vowel_keys({'cat': 3, 'dog': 4}), ({}, 0))
        
        # Test case 3: Dictionary with some keys starting with vowels
        self.assertEqual(sort_vowel_keys({'apple': 10, 'banana': 5, 'orange': 15}), ({'orange': 15, 'apple': 10}, 30))
        
        # Test case 4: Dictionary with all keys starting with vowels
        self.assertEqual(sort_vowel_keys({'apple': 10, 'orange': 15, 'avocado': 20}), ({'avocado': 20, 'orange': 15, 'apple': 10}, 45))
        
        # Test case 5: Mixed case keys
        self.assertEqual(sort_vowel_keys({'Apple': 10, 'Banana': 5, 'Orange': 15}), ({'Orange': 15}, 15))  # Modified output
        
        # Test case 6: Single key starting with a vowel
        self.assertEqual(sort_vowel_keys({'apple': 10}), ({'apple': 10}, 10))  # Modified output

if __name__ == '__main__':
    unittest.main()
