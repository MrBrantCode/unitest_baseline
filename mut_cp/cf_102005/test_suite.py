from solution import is_prime
### test cases
import unittest

class TestSumPrimes(unittest.TestCase):
    """
    Test class for the sum_primes function.
    This class contains several test cases to ensure the sum_primes function works correctly.
    """

    def test_empty_list(self):
        """
        Test case for an empty list.
        Expected result: 0
        """
        self.assertEqual(sum_primes([]), 0)

    def test_no_primes(self):
        """
        Test case for a list with no prime numbers.
        Expected result: 0
        """
        self.assertEqual(sum_primes([4, 6, 8]), 0)

    def test_all_primes(self):
        """
        Test case for a list with only prime numbers.
        Expected result: sum of all prime numbers in the list
        """
        self.assertEqual(sum_primes([2, 3, 5, 7]), 17)

    def test_mixed_numbers(self):
        """
        Test case for a list with both prime and non-prime numbers.
        Expected result: sum of all prime numbers in the list
        """
        self.assertEqual(sum_primes([10, 11, 12, 13, 14, 15, 16, 17]), 41)

    def test_single_element_list(self):
        """
        Test case for a list with a single element.
        Expected result: the element itself if it's prime, otherwise 0
        """
        self.assertEqual(sum_primes([2]), 2)
        self.assertEqual(sum_primes([4]), 0)

    def test_large_numbers(self):
        """
        Test case for a list with large prime numbers.
        Expected result: sum of all prime numbers in the list
        """
        self.assertEqual(sum_primes([101, 103, 107, 109, 113]), 533)  # Sum of first 5 prime numbers > 100

if __name__ == '__main__':
    unittest.main()
