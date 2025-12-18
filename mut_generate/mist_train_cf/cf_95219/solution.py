"""
QUESTION:
Create a function named `prime_numbers` that takes two parameters, `x` and `y`, where `x` is less than or equal to `y`, and returns a list of all prime numbers between `x` and `y` (inclusive). The function should only return prime numbers in the given range.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_numbers(x, y):
    primes = []
    for num in range(x, y+1):
        if is_prime(num):
            primes.append(num)
    return primes