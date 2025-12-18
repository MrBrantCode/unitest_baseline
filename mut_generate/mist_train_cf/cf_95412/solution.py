"""
QUESTION:
Write a function `sieve_of_eratosthenes(n)` to find all prime numbers up to `n` with a time complexity of O(n log n) or better. The function should take an integer `n` as input and return a list of prime numbers up to `n`.
"""

import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    limit = math.isqrt(n)
    for i in range(2, limit + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]