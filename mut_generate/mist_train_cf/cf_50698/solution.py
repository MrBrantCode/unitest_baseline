"""
QUESTION:
Implement a function named `SieveOfEratosthenes` that takes two arguments, `n` and `m`, representing a range of numbers, and returns a list of all prime numbers within that range. The function should use the Sieve of Eratosthenes algorithm to find the prime numbers. The input range is inclusive of `n` but exclusive of `m+1`.
"""

def SieveOfEratosthenes(n, m):
    primes = [True for i in range(m+1)]
    p = 2
    while (p**2 <= m):
        if (primes[p] == True):
            for i in range(p**2, m+1, p):
                primes[i] = False
        p += 1
    return [p for p in range(n, m) if primes[p]]