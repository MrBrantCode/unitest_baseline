from solution import calculate_numbers
### test cases
import unittest

class TestCalculateNumbers(unittest.TestCase):
    def test_positive_integer(self):
        # Test with a positive integer
        result = calculate_numbers(123)
        self.assertEqual(result, (6, math.factorial(1) + math.factorial(2) + math.factorial(3)))
    
    def test_single_digit(self):
        # Test with a single digit number
        result = calculate_numbers(5)
        self.assertEqual(result, (5, math.factorial(5)))
    
    def test_large_number(self):
        # Test with a large number
        result = calculate_numbers(987654321)
        expected_total = sum([int(x) for x in str(987654321)])
        expected_factorial_sum = sum(math.factorial(int(x)) for x in str(987654321))
        self.assertEqual(result, (45, expected_factorial_sum))
    
    def test_zero(self):
        # Test with zero, which should return an error message
        result = calculate_numbers(0)
        self.assertEqual(result, "Input should be a positive integer")
    
    def test_negative_number(self):
        # Test with a negative number, which should return an error message
        result = calculate_numbers(-123)
        self.assertEqual(result, "Input should be a positive integer")
    
    def test_non_integer_input(self):
        # Test with a non-integer input, which should return an error message
        result = calculate_numbers(12.34)
        self.assertEqual(result, "Input should be a positive integer")
    
    def test_string_input(self):
        # Test with a string input, which should return an error message
        result = calculate_numbers("abc")
        self.assertEqual(result, "Input should be a positive integer")  # Modified output

if __name__ == '__main__':
    unittest.main()
