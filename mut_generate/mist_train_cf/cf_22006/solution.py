"""
QUESTION:
Write a function named `sum_of_cubed_primes` that calculates the sum of the cube of prime numbers from 1 to a given positive integer `n`. The function should take an integer `n` as input and return the sum of the cubes of all prime numbers between 1 and `n` (inclusive).
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_cubed_primes(n):
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    sum_of_cubes = sum([prime**3 for prime in primes])
    return sum_of_cubes