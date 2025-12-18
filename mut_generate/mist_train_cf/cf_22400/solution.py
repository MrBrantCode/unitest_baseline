"""
QUESTION:
Write a function `prime_factors(n)` that computes the prime factors of a given positive integer `n` in O(sqrt(n)) time complexity, where `n` is the input integer. The function should return a list of prime factors.
"""

import math

def prime_factors(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors