"""
QUESTION:
Write a function called `get_prime_factors(n)` that returns a list of all prime factors of a given integer `n`, where `n` can be as large as 10^15.
"""

import math

def get_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors