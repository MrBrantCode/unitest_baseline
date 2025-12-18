"""
QUESTION:
Write a function `partition_numbers` that takes a list of integers as input and returns two lists: one containing the prime numbers and the other containing the composite numbers. The function should ignore negative numbers and zeros.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def partition_numbers(lst):
    primes = []
    composites = []
    for num in lst:
        if num > 1:
            if is_prime(num):
                primes.append(num)
            else:
                composites.append(num)
    return primes, composites