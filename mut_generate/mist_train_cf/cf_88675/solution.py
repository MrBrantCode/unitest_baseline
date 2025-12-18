"""
QUESTION:
Create a function named `sum_of_cubes_of_primes` that takes an integer `n` as input and returns the sum of the cubes of all prime numbers up to `n`. The function must implement the Sieve of Eratosthenes algorithm to find all prime numbers up to `n`.
"""

import math

def sum_of_cubes_of_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, math.isqrt(n) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    sum_of_cubes = 0
    for i in range(n + 1):
        if primes[i]:
            sum_of_cubes += i**3

    return sum_of_cubes