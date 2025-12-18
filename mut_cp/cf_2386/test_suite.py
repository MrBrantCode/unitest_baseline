from solution import is_prime
### test case
import unittest

class TestProcessPrimeNumbers(unittest.TestCase):
    def test_single_prime(self):
        # Test with a single prime number
        result = process_prime_numbers([5])
        self.assertEqual(result, (5, 5, 5, 5))

    def test_multiple_primes(self):
        # Test with multiple prime numbers
        result = process_prime_numbers([2, 3, 5, 7, 11])
        self.assertEqual(result, (28, 7.0, 11, 2))

    def test_mixed_numbers(self):
        # Test with a mix of prime and non-prime numbers
        result = process_prime_numbers([4, 6, 8, 10, 11, 13])
        self.assertEqual(result, (24, 12.0, 13, 11))

    def test_negative_numbers(self):
        # Test with negative numbers (no negative primes)
        result = process_prime_numbers([-2, -3, -5, 7])
        self.assertEqual(result, (7, 7.0, 7, 7))

    def test_zero_and_one(self):
        # Test with zero and one (not prime)
        result = process_prime_numbers([0, 1, 2, 3])
        self.assertEqual(result, (5, 5.0, 3, 2))  # Modified output

    def test_large_numbers(self):
        # Test with large prime numbers
        result = process_prime_numbers([101, 103, 107, 109])
        self.assertEqual(result, (420, 105.0, 109, 101))  # Modified output

if __name__ == '__main__':
    unittest.main()
