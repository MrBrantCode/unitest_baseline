"""
QUESTION:
Create a function `get_smallest_prime_divisor(n)` that takes an integer `n` as input and returns the smallest prime divisor of `n` if `n` is composite, or `n` itself if `n` is prime. The function should only check divisibility up to the square root of `n`. Also, create a function `is_prime(n)` to check if `n` is prime or composite. Assume that the input integer `n` is between 1 and 1000.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_smallest_prime_divisor(n):
    if is_prime(n):
        return n
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return i
        i += 1