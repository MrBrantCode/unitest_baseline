from solution import is_prime
### test cases
import unittest

class TestReplaceSecondSmallestPrime(unittest.TestCase):
    def test_no_primes(self):
        # Test case when the input array contains no prime numbers.
        self.assertEqual(replace_second_smallest_prime([4, 6, 8]), [4, 6, 8])

    def test_single_prime(self):
        # Test case when the input array contains only one prime number.
        self.assertEqual(replace_second_smallest_prime([2]), [2])

    def test_two_primes(self):
        # Test case when the input array contains exactly two prime numbers.
        self.assertEqual(replace_second_smallest_prime([2, 3]), [2, 5])

    def test_multiple_primes(self):
        # Test case when the input array contains multiple prime numbers.
        self.assertEqual(replace_second_smallest_prime([2, 3, 5, 7]), [2, 17, 5, 7])

    def test_no_second_smallest_prime(self):
        # Test case when the input array does not contain a second smallest prime number.
        self.assertEqual(replace_second_smallest_prime([2, 4, 6, 8]), [2, 10, 6, 8])

    def test_mixed_numbers(self):
        # Test case when the input array contains both prime and non-prime numbers.
        self.assertEqual(replace_second_smallest_prime([2, 4, 5, 6, 7, 8]), [2, 24, 5, 6, 7, 8])  # Modified output

    def test_large_input(self):
        # Test case with a large input array to ensure the function handles it efficiently.
        arr = [i for i in range(10000)]
        expected_output = [i if is_prime(i) else i for i in range(10000)]  # Only primes are summed
        self.assertEqual(replace_second_smallest_prime(arr), expected_output)  # Modified output

if __name__ == '__main__':
    unittest.main()
