"""
QUESTION:
Create a function called `sieve_of_eratosthenes` that takes an integer `n` as input and returns a list of all prime numbers less than or equal to `n`. The function should minimize repetitive computations by only checking divisibility up to the square root of each number. The input `n` can be as large as 10^6, so the function should have excellent time and space complexity.
"""

def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while p**2 <= n:
        if primes[p] is True:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    primes_only = [p for p in range(2, n+1) if primes[p]]
    return primes_only