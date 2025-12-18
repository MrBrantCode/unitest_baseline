"""
QUESTION:
Write a function `get_smallest_prime_divisor(n)` that takes a positive integer `n` and returns the smallest prime number that divides `n`. If `n` is a prime number, return `n` itself. The function should only check divisibility up to the square root of `n`.
"""

import math

def get_smallest_prime_divisor(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return i
        i += 1
    return n