"""
QUESTION:
Write a function `sieve_of_eratosthenes` that finds all prime numbers up to a given number `n`. Implement another function `is_prime` to validate the found numbers. Optimize the algorithm for time efficiency to support further increase in the range of numbers.
"""

import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    """Find all prime numbers up to a given number n using the Sieve of Eratosthenes algorithm."""
    primes = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers