"""
QUESTION:
Create a function named `is_perfect_square_and_prime` that takes an integer `num` as input and returns `True` if `num` is both a perfect square and a prime number, and `False` otherwise. The function should check if `num` is a perfect square and then verify if it is a prime number.
"""

import math

def is_perfect_square_and_prime(num):
    if math.isqrt(num) ** 2 == num:
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False