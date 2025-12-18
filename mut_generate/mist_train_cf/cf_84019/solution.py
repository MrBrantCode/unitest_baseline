"""
QUESTION:
Write a function named `first_primes` that returns a list of the first `n` prime numbers using the Sieve of Eratosthenes algorithm. The function should not take a maximum limit as input, but instead should dynamically adjust its search space to find the required number of primes.
"""

def first_primes(num_primes):
    n = 30  # Start with a guess
    primes = []
    while len(primes) < num_primes:
        primes = sieve_of_eratosthenes(n)
        n *= 2  # Double the search space each time

    return primes[:num_primes]


def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    primes_only = [p for p in range(2, n) if primes[p]]
    return primes_only