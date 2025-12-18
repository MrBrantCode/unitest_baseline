"""
QUESTION:
Create a function `is_mersenne_prime(n)` that takes a positive integer `n` as input and returns `True` if `n` is a Mersenne prime, `False` otherwise. A Mersenne prime is a prime number that is one less than a power of two, i.e., it can be written in the form `2^p - 1`, where `p` is also a prime number.
"""

import math

def is_mersenne_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        max_divisor = math.isqrt(num)
        for d in range(3, 1 + max_divisor, 2):
            if num % d == 0:
                return False
        return True

    p = 2
    while True:
        mersenne_number = 2**p - 1
        if mersenne_number == n and is_prime(p) and is_prime(n):
            return True
        elif mersenne_number > n:
            return False
        p += 1