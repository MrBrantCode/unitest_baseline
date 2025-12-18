"""
QUESTION:
Create a function named `get_primes_in_range` that takes two parameters, `start` and `end`, representing a range of numbers. The function should return a list of prime numbers within the range, sorted in ascending order.
"""

import math

def get_primes_in_range(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    return sorted([x for x in range(start, end + 1) if is_prime(x)])