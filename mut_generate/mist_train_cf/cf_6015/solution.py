"""
QUESTION:
Implement a function called `sieve_of_eratosthenes` that takes an integer `limit` as input, and returns a list of all prime numbers up to `limit` without duplicates, ensuring the function runs in linear time complexity.
"""

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit+1)
    primes[0] = primes[1] = False

    p = 2
    while p*p <= limit:
        if primes[p]:
            for i in range(p*p, limit+1, p):
                primes[i] = False
        p += 1

    return [i for i in range(limit+1) if primes[i]]