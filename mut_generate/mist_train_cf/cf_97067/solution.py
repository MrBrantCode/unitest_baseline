"""
QUESTION:
Write a function `prime_factors(n)` that takes a positive integer `n` as input and returns a list of its prime factors in O(sqrt(n)) time complexity. The function should iterate up to the square root of `n` and return all prime factors, including duplicate factors. If `n` itself is a prime number, it should be included in the output list.
"""

import math

def entance(n):
    factors = []
    # Check for factors up to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is still greater than 1, n itself is a prime factor
    if n > 1:
        factors.append(n)
    return factors