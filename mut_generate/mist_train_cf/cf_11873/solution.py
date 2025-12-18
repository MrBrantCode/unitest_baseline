"""
QUESTION:
Write a function called `find_primes` that takes two integers `lower` and `upper` as input, representing the lower and upper bounds of a range, and returns a list of all prime numbers within that range. The function should have a time complexity of O(n√m), where n is the size of the range and m is the upper bound.
"""

import math

def find_primes(lower, upper):
    """
    Returns a list of all prime numbers within the given range.

    Time complexity: O(n√m), where n is the size of the range and m is the upper bound.

    Args:
        lower (int): The lower bound of the range (inclusive).
        upper (int): The upper bound of the range (inclusive).

    Returns:
        list: A list of prime numbers within the given range.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in range(lower, upper + 1) if is_prime(num)]
    return primes