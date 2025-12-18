from solution import extract_primes
### test cases
import unittest

class TestExtractPrimes(unittest.TestCase):
    """
    Test class for the extract_primes function.
    """

    def test_empty_list(self):
        """
        Test with an empty list.
        Expected result: []
        """
        self.assertEqual(extract_primes([]), [])

    def test_single_prime_number(self):
        """
        Test with a single prime number.
        Expected result: [2]
        """
        self.assertEqual(extract_primes([2]), [2])

    def test_single_non_prime_number(self):
        """
        Test with a single non-prime number.
        Expected result: []
        """
        self.assertEqual(extract_primes([4]), [])

    def test_mixed_numbers(self):
        """
        Test with a list containing both prime and non-prime numbers.
        Expected result: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        """
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]
        expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(extract_primes(numbers), expected_result)

    def test_large_numbers(self):
        """
        Test with a list containing large prime numbers.
        Expected result: [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
        """

if __name__ == '__main__':
    unittest.main()
