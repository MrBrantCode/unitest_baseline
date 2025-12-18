"""
QUESTION:
Create a function `is_prime(n)` that checks if a given number `n` is prime or not and another function `find_primes(start, end)` that takes a range of numbers as input and returns a list of all prime numbers within that range. The function `find_primes(start, end)` should return an empty list if the input range is invalid, i.e., `start` is greater than or equal to `end`.
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
    if start >= end:
        return []
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes