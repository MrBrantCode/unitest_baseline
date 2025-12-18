from solution import find_duplicates
### test cases
import unittest

class TestFindDuplicates(unittest.TestCase):
    def test_empty_array(self):
        # Test case for an empty array
        self.assertEqual(find_duplicates([]), [])
        
    def test_no_duplicates(self):
        # Test case for an array with no duplicate elements
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])
        
    def test_all_duplicates(self):
        # Test case for an array where all elements are duplicates
        self.assertEqual(find_duplicates([1, 1, 1, 1, 1]), [1])
        
    def test_mixed_duplicates(self):
        # Test case for an array with mixed duplicate and non-duplicate elements
        self.assertEqual(find_duplicates([1, 2, 2, 3, 4, 4, 5]), [2, 4])
        
    def test_large_array(self):
        # Test case for a large array (approaching the maximum limit of 10^5)
        arr = list(range(100000)) + [99999] * 1000
        self.assertEqual(find_duplicates(arr), [99999])  # Modified output
        
    def test_negative_numbers(self):
        # Test case for an array containing negative numbers
        self.assertEqual(find_duplicates([-1, -2, -2, -3, -4, -4, -5]), [-2, -4])
        
    def test_mixed_signs(self):
        # Test case for an array containing both positive and negative numbers
        self.assertEqual(find_duplicates([-1, 2, 2, -3, 4, 4, -5]), [2, 4])  # Modified output

if __name__ == '__main__':
    unittest.main()
