"""
QUESTION:
Write a function `is_mersenne_prime(n)` to determine if a given integer `n` is a Mersenne prime number, which is a prime number of the form `2^p - 1` for some integer `p`, where `p` is also a prime number. The function should return `True` if `n` is a Mersenne prime, and `False` otherwise.
"""

import math

def is_mersenne_prime(n):
    if n < 2:
        return False

    def is_prime(p):
        if p == 1 or (p % 2 == 0 and p > 2):
            return False
        else:
            sqrtp = math.isqrt(p)
            for divisor in range(3, sqrtp + 1, 2):
                if p % divisor == 0:
                    return False
            return True

    p = math.log2(n + 1)
    if p.is_integer():

        # Check if p is prime
        if is_prime(int(p)):
            return True
    return False