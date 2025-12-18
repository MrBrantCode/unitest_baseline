from solution import get_unique_odd_numbers
### test cases
import unittest

class TestGetUniqueOddNumbers(unittest.TestCase):
    def test_empty_list(self):
        # Test with an empty list, should return an empty list
        self.assertEqual(get_unique_odd_numbers([]), [])
    
    def test_no_odd_numbers(self):
        # Test with a list containing only even numbers, should return an empty list
        self.assertEqual(get_unique_odd_numbers([2, 4, 6, 8]), [])
    
    def test_all_odd_numbers(self):
        # Test with a list containing only odd numbers, should return the same list in descending order
        self.assertEqual(get_unique_odd_numbers([1, 3, 5, 7]), [7, 5, 3, 1])
    
    def test_mixed_numbers(self):
        # Test with a list containing both odd and even numbers, should return unique odd numbers in descending order
        self.assertEqual(get_unique_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), [9, 7, 5, 3, 1])
    
    def test_duplicate_odd_numbers(self):
        # Test with a list containing duplicate odd numbers, should return unique odd numbers in descending order
        self.assertEqual(get_unique_odd_numbers([1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9]), [9, 7, 5, 3, 1])  # Modified output
    
    def test_negative_numbers(self):
        # Test with a list containing negative numbers, should return unique odd numbers in descending order
        self.assertEqual(get_unique_odd_numbers([-1, -2, -3, -4, -5]), [-1, -3, -5])  # Modified output
    
    def test_large_input(self):
        # Test with a large list of numbers, should return unique odd numbers in descending order
        nums = list(range(10000))

if __name__ == '__main__':
    unittest.main()
