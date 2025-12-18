from solution import sum_between_10_and_20
### test cases
import unittest

class TestSumBetween10And20(unittest.TestCase):
    """
    Test class for the function 'sum_between_10_and_20'. This class contains several test cases to ensure the function works as expected.
    """

    def test_empty_array(self):
        # Test case for an empty array
        self.assertEqual(sum_between_10_and_20([]), 0)

    def test_no_numbers_in_range(self):
        # Test case for an array with no numbers between 10 and 20
        self.assertEqual(sum_between_10_and_20([1, 2, 3, 4, 5]), 0)

    def test_numbers_in_range(self):
        # Test case for an array with numbers between 10 and 20
        self.assertEqual(sum_between_10_and_20([11, 12, 15, 18]), 56)

    def test_mixed_numbers(self):
        # Test case for an array with both numbers in and out of the range
        self.assertEqual(sum_between_10_and_20([8, 11, 14, 17, 21, 25]), 42)

    def test_single_number_in_range(self):
        # Test case for an array with a single number between 10 and 20
        self.assertEqual(sum_between_10_and_20([15]), 15)  # Modified output

    def test_negative_numbers(self):
        # Test case for an array with negative numbers
        self.assertEqual(sum_between_10_and_20([-10, -5, 0, 5, 10]), 0)

    def test_large_numbers(self):
        # Test case for an array with large numbers
        self.assertEqual(sum_between_10_and_20([100, 200, 300, 400, 500]), 0)  # Modified output

if __name__ == '__main__':
    unittest.main()
