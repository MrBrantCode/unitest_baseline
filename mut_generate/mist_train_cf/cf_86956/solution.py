"""
QUESTION:
Create a function `is_prime(n)` to determine if a number `n` is prime and use it in another function `find_primes(start, end)` to find all prime numbers within the range from `start` to `end` (inclusive) and return them in a list in ascending order. The `is_prime(n)` function should return `True` if `n` is prime and `False` otherwise.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes