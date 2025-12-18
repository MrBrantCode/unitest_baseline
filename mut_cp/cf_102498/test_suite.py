from solution import findMax
### test cases
import unittest

class TestFindMax(unittest.TestCase):
    def test_empty_array(self):
        # Test case for an empty array
        self.assertIsNone(findMax([]))
    
    def test_all_elements_same(self):
        # Test case for an array with all elements being the same
        self.assertEqual(findMax([5, 5, 5, 5]), 5)
    
    def test_all_negative_elements(self):
        # Test case for an array with all elements being negative
        self.assertEqual(findMax([-3, -2, -1, -4]), -1)
    
    def test_all_positive_elements(self):
        # Test case for an array with all elements being positive
        self.assertEqual(findMax([1, 2, 3, 4]), 4)
    
    def test_mixed_elements(self):
        # Test case for an array with mixed positive and negative elements
        self.assertEqual(findMax([-10, 20, -30, 40, 50]), 50)
    
    def test_single_element(self):
        # Test case for an array with a single element
        self.assertEqual(findMax([42]), 42)

if __name__ == '__main__':
    unittest.main()
