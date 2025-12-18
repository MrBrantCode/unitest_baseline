"""
QUESTION:
Write a function named `primes_sum` that calculates the sum of all prime numbers within a given range up to 10^6, optimizing the code for the least possible execution time. The function should take an integer `n` as input and return the sum of all prime numbers less than `n`.
"""

def primes_sum(n):
    sieve = [True] * (n+1)
    p = 2
    while (p * p <= n):
        if (sieve[p] == True):
            for i in range(p * p, n+1, p):
                sieve[i] = False
        p += 1
    primes = [p for p in range(2, n) if sieve[p]]
    return sum(primes)