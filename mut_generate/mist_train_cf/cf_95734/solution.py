"""
QUESTION:
Create a function `find_primes(n)` that finds all prime numbers from 1 to `n` (inclusive) using the Sieve of Eratosthenes algorithm and returns them in a list. The input `n` is a positive integer. The function should be able to handle inputs up to at least 100.
"""

def find_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    result = [i for i in range(n + 1) if primes[i]]
    return result