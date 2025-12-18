from solution import count_digit_occurrences
### test cases
import unittest

class TestCountDigitOccurrences(unittest.TestCase):
    """
    This test class contains several test cases to ensure the correctness of the count_digit_occurrences function.
    Each test case checks the function with different inputs to verify its behavior.
    """

    def test_single_digit(self):
        # Test when the range has only one number
        self.assertEqual(count_digit_occurrences(5, 5, 5), 1)

    def test_multiple_digits(self):
        # Test when the range includes multiple numbers with the target digit
        self.assertEqual(count_digit_occurrences(10, 15, 1), 2)

    def test_no_occurrence(self):
        # Test when there are no occurrences of the target digit in the range
        self.assertEqual(count_digit_occurrences(20, 25, 6), 0)

    def test_large_range(self):
        # Test with a larger range of numbers
        self.assertEqual(count_digit_occurrences(100, 110, 1), 3)

    def test_edge_cases(self):
        # Test edge cases like when start is greater than end
        self.assertEqual(count_digit_occurrences(10, 9, 1), 0)
        self.assertEqual(count_digit_occurrences(10, 10, 2), 0)  # No occurrence of 2 in 10

    def test_zero_included(self):
        # Test when zero is included in the range
        self.assertEqual(count_digit_occurrences(0, 10, 0), 2)  # Zero occurs twice in 0-10 (0 and 10)  # Modified output

if __name__ == '__main__':
    unittest.main()
