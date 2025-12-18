"""
QUESTION:
Write a Python function `find_primes_within_range(start, end)` that determines all the prime numbers within a given range `[start, end]` where `start` and `end` are integers. The function should return a list of prime numbers within this range. 

Note: The function `is_prime(n)` can be used as a helper function to check if a number `n` is prime. The `is_prime(n)` function should only check divisibility up to the square root of `n` to optimize the solution.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_within_range(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes