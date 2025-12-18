"""
QUESTION:
Create a function `is_perfect_square_and_prime(num)` that checks if a given integer `num` is both a perfect square and a prime number. The function should return `True` if both conditions are met, and `False` otherwise.
"""

import math

def is_perfect_square_and_prime(num):
    # Check if the number is a perfect square
    if math.isqrt(num) ** 2 == num:
        # Check if the number is prime
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False