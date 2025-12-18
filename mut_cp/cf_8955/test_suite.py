from solution import find_prime_factors
### test cases
import unittest

class TestFindPrimeFactors(unittest.TestCase):
    """
    Test class for the find_prime_factors function.
    """

    def test_single_prime_factor(self):
        """
        Test case where the input number has only one prime factor (itself).
        """
        self.assertEqual(find_prime_factors(7), [7])

    def test_multiple_prime_factors(self):
        """
        Test case where the input number has multiple prime factors.
        """
        self.assertEqual(find_prime_factors(100), [2, 2, 5, 5])

    def test_prime_number(self):
        """
        Test case where the input number itself is a prime number.
        """
        self.assertEqual(find_prime_factors(13), [13])

    def test_one(self):
        """
        Test case where the input number is 1, which has no prime factors.
        """
        self.assertEqual(find_prime_factors(1), [])

    def test_even_number(self):
        """
        Test case where the input number is an even number with multiple prime factors.
        """
        self.assertEqual(find_prime_factors(60), [2, 2, 3, 5])  # Modified output

    def test_odd_number(self):
        """
        Test case where the input number is an odd number with multiple prime factors.
        """
        self.assertEqual(find_prime_factors(105), [3, 5, 7])  # Modified output

if __name__ == '__main__':
    unittest.main()
