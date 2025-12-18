"""
QUESTION:
Write a function to find all prime factors of a given integer up to 10^12. The function should return a list of prime factors.

The input integer can be as large as 10^12. Exclude any code snippet and reference in the function definition.
"""

import math

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors