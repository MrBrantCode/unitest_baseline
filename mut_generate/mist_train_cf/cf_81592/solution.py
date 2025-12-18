"""
QUESTION:
Write a function `sieve_of_eratosthenes(n)` that takes an integer `n` as input, generates all prime numbers under `n`, categorizes them into safe primes and non-safe primes, and calculates the product of all primes. A safe prime is a prime number that is two less than another prime number. The function should return the product of all prime numbers and categorize them into two lists of safe primes and non-safe primes. The function should be optimized for maximum efficiency and performance.
"""

import math

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, n):
        if primes[p]:
            prime_numbers.append(p)
    product = 1
    safe_primes = []
    non_safe_primes = []
    for prime in prime_numbers:
        product *= prime
        if prime - 2 in prime_numbers:
            safe_primes.append(prime)
        else:
            non_safe_primes.append(prime)
    return product, safe_primes, non_safe_primes