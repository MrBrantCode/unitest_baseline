from solution import find_median
### test cases
import unittest

class TestFindMedian(unittest.TestCase):
    def test_odd_length_list(self):
        # Test case for a list with an odd number of elements
        self.assertEqual(find_median([3, 1, 2]), 2)

    def test_even_length_list(self):
        # Test case for a list with an even number of elements
        self.assertEqual(find_median([10, 20, 30, 40]), 25)

    def test_empty_list(self):
        # Test case for an empty list
        self.assertIsNone(find_median([]))

    def test_non_integer_elements(self):
        # Test case for a list containing non-integer elements
        self.assertIsNone(find_median([1, 2, 'a', 3]))

    def test_duplicates(self):
        # Test case for a list with duplicate elements
        self.assertEqual(find_median([1, 2, 2, 3, 4]), 2)

    def test_single_element(self):
        # Test case for a list with a single element
        self.assertEqual(find_median([42]), 42)

    def test_mixed_types(self):
        # Test case for a list with mixed types (integers and non-integers)
        self.assertIsNone(find_median([1, 'a', 2, 'b', 3]))  # Modified output

if __name__ == '__main__':
    unittest.main()
