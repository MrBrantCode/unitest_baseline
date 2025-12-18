"""
QUESTION:
Create a function `find_primes(n)` that returns a list of all prime numbers from 1 to `n` (inclusive) using a mathematical algorithm.
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

    result = []
    for i in range(n + 1):
        if primes[i]:
            result.append(i)

    return result