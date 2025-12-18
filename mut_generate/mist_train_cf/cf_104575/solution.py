"""
QUESTION:
Create a function named `is_prime_and_perfect_square` that takes a positive integer `num` as input and returns `True` if `num` is both a prime number and a perfect square, and `False` otherwise. Note that the function should consider 1 as neither a prime number nor a perfect square.
"""

import math

def is_prime_and_perfect_square(num):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect_square(n):
        sqrt = math.sqrt(n)
        return sqrt.is_integer()

    return is_prime(num) and is_perfect_square(num)