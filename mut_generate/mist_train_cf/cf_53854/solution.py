"""
QUESTION:
Create a function called `largest_prime_factor` that takes an integer `n` as input and returns the largest prime factor of `n` that is less than `n`. The function should be efficient and only check divisors up to the square root of `n`.
"""

import math

def largest_prime_factor(n):
    # Start from the smallest prime number, which is 2.
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n