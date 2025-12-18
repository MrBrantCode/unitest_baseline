"""
QUESTION:
Create a function `is_prime(n)` to check if a number `n` is prime and a function `find_primes(start, end)` to find all prime numbers within a given range `[start, end]` (inclusive). `find_primes(start, end)` should return a list of prime numbers in ascending order. Assume `start` and `end` are non-negative integers and `start` is less than or equal to `end`.
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