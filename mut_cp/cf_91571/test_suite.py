from solution import flatten_and_remove_duplicates
### test cases
import unittest

class TestFlattenAndRemoveDuplicates(unittest.TestCase):
    def test_empty_array(self):
        # Test case for an empty 2D array
        self.assertEqual(flatten_and_remove_duplicates([]), [])

    def test_single_element(self):
        # Test case for a 2D array with a single element
        self.assertEqual(flatten_and_remove_duplicates([[1]]), [1])

    def test_no_duplicates(self):
        # Test case for a 2D array with no duplicate elements
        self.assertEqual(flatten_and_remove_duplicates([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_with_duplicates(self):
        # Test case for a 2D array with duplicate elements
        self.assertEqual(flatten_and_remove_duplicates([[1, 2, 2], [3, 4, 4]]), [1, 2, 3, 4])

    def test_negative_numbers(self):
        # Test case for a 2D array containing negative numbers
        self.assertEqual(flatten_and_remove_duplicates([[-1, -2], [-3, -4]]), [-4, -3, -2, -1])

    def test_mixed_signs(self):
        # Test case for a 2D array containing both positive and negative numbers
        self.assertEqual(flatten_and_remove_duplicates([[1, -2], [3, -4]]), [-4, -2, 1, 3])

    def test_large_input(self):
        # Test case for a large 2D array
        large_input = [[i for i in range(10000)] for _ in range(10)]
        expected_output = list(range(10000))
        self.assertEqual(flatten_and_remove_duplicates(large_input), expected_output)  # Modified output

if __name__ == '__main__':
    unittest.main()
