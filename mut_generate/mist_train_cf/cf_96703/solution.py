"""
QUESTION:
Write a function `is_prime_range` that takes two parameters, `start` and `end`, representing the start and end of a range of integers. The function should return a list of prime numbers within this range, sorted in ascending order.
"""

import math

def is_prime_range(start, end):
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