"""
QUESTION:
Create a function `is_prime_gt_100` that checks if a given integer value is a prime number greater than 100. The function should return `True` if the number is prime and greater than 100, and `False` otherwise. The function should optimize the prime check by only testing divisors up to the square root of the given value.
"""

import math

def is_prime_gt_100(value):
    if value <= 100:
        return False

    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False

    return True