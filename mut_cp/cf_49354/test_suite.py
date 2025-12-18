from solution import get_even_keys_in_reverse
### test cases
import unittest

class TestGetEvenKeysInReverse(unittest.TestCase):
    def test_empty_dict(self):
        # Test case for an empty dictionary
        self.assertEqual(get_even_keys_in_reverse({}), [])
        
    def test_no_even_values(self):
        # Test case for a dictionary with no keys having even values
        self.assertEqual(get_even_keys_in_reverse({'a': 1, 'b': 3, 'c': 5}), [])
        
    def test_all_even_values(self):
        # Test case for a dictionary with all keys having even values
        self.assertEqual(get_even_keys_in_reverse({'a': 2, 'b': 4, 'c': 6}), ['c', 'b', 'a'])
        
    def test_mixed_values(self):
        # Test case for a dictionary with a mix of even and odd values
        self.assertEqual(get_even_keys_in_reverse({'a': 1, 'b': 2, 'c': 3, 'd': 4}), ['d', 'b'])
        
    def test_single_even_value(self):
        # Test case for a dictionary with only one key having an even value
        self.assertEqual(get_even_keys_in_reverse({'a': 1, 'b': 2}), ['b'])  # Modified output
        
    def test_single_odd_value(self):
        # Test case for a dictionary with only one key having an odd value
        self.assertEqual(get_even_keys_in_reverse({'a': 1}), [])

if __name__ == '__main__':
    unittest.main()
