"""
QUESTION:
Implement the function `sieve_of_eratosthenes(n)` that returns a list of all prime numbers from 0 to `n`, where `n` is an integer greater than 1. The function should have a time complexity of O(n√n) or better.
"""

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]
    return prime_numbers