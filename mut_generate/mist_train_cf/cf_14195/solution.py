"""
QUESTION:
Write a function called `sieve_of_eratosthenes` that uses the Sieve of Eratosthenes algorithm to calculate the sum of all prime numbers between 1 and a given limit `n`, which is 100,000.
"""

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return sum(i for i in range(n + 1) if primes[i])