"""
QUESTION:
Write a function named `product_of_primes_in_range` to calculate the product of all prime numbers within a given range. The function should take two parameters: `start` and `end`, which define the range. The function should return the product of all prime numbers in the range from `start` to `end` (inclusive).
"""

import math

def product_of_primes_in_range(start, end):
    """
    Calculate the product of all prime numbers within a given range.

    Args:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).

    Returns:
    int: The product of all prime numbers in the range from start to end.
    """

    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        sqrt_n = math.isqrt(n) + 1
        for divisor in range(3, sqrt_n, 2):
            if n % divisor == 0:
                return False
        return True

    result = 1
    for number in range(start, end + 1):
        if is_prime(number):
            result *= number
    return result