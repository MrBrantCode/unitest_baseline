from solution import find_median
### test cases
import unittest

class TestFindMedian(unittest.TestCase):
    def test_odd_length_list(self):
        # Test case for a list with an odd number of elements
        self.assertEqual(find_median([3, 1, 2]), 2)

    def test_even_length_list(self):
        # Test case for a list with an even number of elements
        self.assertAlmostEqual(find_median([10, 20, 30, 40]), 25)

    def test_single_element_list(self):
        # Test case for a list with a single element
        self.assertEqual(find_median([5]), 5)

    def test_empty_list(self):
        # Test case for an empty list
        with self.assertRaises(IndexError):
            find_median([])

    def test_duplicate_values(self):
        # Test case for a list with duplicate values
        self.assertEqual(find_median([1, 2, 2, 3, 4]), 2)

    def test_negative_numbers(self):
        # Test case for a list containing negative numbers
        self.assertAlmostEqual(find_median([-10, -20, -30, -40, -50]), -30)

    def test_large_list(self):
        # Test case for a large list
        self.assertAlmostEqual(find_median(list(range(10000))), 4999.5)  # Median of first 10000 natural numbers

if __name__ == '__main__':
    unittest.main()
