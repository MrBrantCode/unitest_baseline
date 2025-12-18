"""
QUESTION:
Write a function named `prime_factors` that takes an integer `n` as input and returns a dictionary where the keys are the prime divisors of `n` and the values are their corresponding multiplicities. The function should have a time complexity better than O(n) and should not use any built-in functions for finding prime factors. The function should only consider prime divisors up to the square root of `n`.
"""

import math

def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] = factors.get(i, 0) + 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors