from solution import flatten_divisible_by_two_and_three
### test cases
import unittest

class TestFlattenDivisibleByTwoAndThree(unittest.TestCase):
    """
    Test class for the flatten_divisible_by_two_and_three function.
    """

    def test_empty_input(self):
        """
        Test with an empty list.
        Expected result: []
        """
        self.assertEqual(flatten_divisible_by_two_and_three([]), [])

    def test_no_divisible_numbers(self):
        """
        Test with a list that contains no numbers divisible by both 2 and 3.
        Expected result: []
        """
        self.assertEqual(flatten_divisible_by_two_and_three([[1, 5, 7], [11, 13]]), [])

    def test_with_divisible_numbers(self):
        """
        Test with a list that contains numbers divisible by both 2 and 3.
        Expected result: [6, 12]
        """
        self.assertEqual(flatten_divisible_by_two_and_three([[2, 3, 6], [8, 9, 12]]), [6, 12])

    def test_mixed_input(self):
        """
        Test with a mixed list that contains both divisible and non-divisible numbers.
        Expected result: [6, 12]
        """
        self.assertEqual(flatten_divisible_by_two_and_three([[1, 2, 3, 4, 6], [7, 8, 9, 10, 12]]), [6, 12])

    def test_negative_numbers(self):
        """
        Test with negative numbers.
        Expected result: [-6, -12]
        """
        self.assertEqual(flatten_divisible_by_two_and_three([[-2, -3, -6], [-8, -9, -12]]), [-6, -12])  # Modified output

    def test_large_numbers(self):
        """
        Test with large numbers.
        Expected result: [6, 12, 18, 24, 30]
        """
        self.assertEqual(flatten_divisible_by_two_and_three([[6, 12, 18], [24, 30, 36]]), [6, 12, 18, 24, 30])  # Modified output

if __name__ == '__main__':
    unittest.main()
