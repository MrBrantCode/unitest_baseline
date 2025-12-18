"""
QUESTION:
Write a function named `power` that calculates the exponentiation of a base number `n` to a specified power `m`, where `n` is an integer between 1 and 10, and `m` is a prime number less than 20. The function should use memoization to optimize the calculation.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return power(base, exponent // 2) ** 2
    else:
        return base * power(base, exponent // 2) ** 2