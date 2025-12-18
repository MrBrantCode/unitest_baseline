"""
QUESTION:
Create a function named `sieve_of_eratosthenes` that generates the first 1000 prime numbers with a time complexity of O(n log n) or better. The input to the function should be an integer `n` that is at least 1000, and the output should be a list of the first 1000 prime numbers. The function should not take any additional arguments other than `n`.
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