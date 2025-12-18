from solution import compare_numbers
### test cases
import unittest

class TestCompareNumbers(unittest.TestCase):
    """
    Test class for the compare_numbers function.
    """

    def test_equal_numbers(self):
        """
        Test case where both numbers are equal.
        Expected output: 0
        """
        self.assertEqual(compare_numbers(10, 10), 0)

    def test_num1_multiple_of_num2(self):
        """
        Test case where num1 is a multiple of num2.
        Expected output: 1
        """
        self.assertEqual(compare_numbers(15, 5), 1)

    def test_num1_not_multiple_of_num2(self):
        """
        Test case where num1 is not a multiple of num2.
        Expected output: -1
        """
        self.assertEqual(compare_numbers(7, 3), -1)

    def test_zero_division(self):
        """
        Test case where either num1 or num2 is zero.
        Expected output: -1
        """
        self.assertEqual(compare_numbers(0, 5), -1)
        self.assertEqual(compare_numbers(5, 0), -1)

    def test_both_zeros(self):
        """
        Test case where both num1 and num2 are zero.
        Expected output: 0
        """
        self.assertEqual(compare_numbers(0, 0), 0)  # Modified output

    def test_negative_numbers(self):
        """
        Test case with negative numbers.
        Expected output: 1 (since the absolute values are considered)
        """
        self.assertEqual(compare_numbers(-20, -4), 1)  # Modified output

if __name__ == '__main__':
    unittest.main()
