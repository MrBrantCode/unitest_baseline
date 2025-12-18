"""
QUESTION:
Create a function `calculate_primes(n)` that takes an integer `n` as input and returns a list of all prime numbers less than `n`. The function should be implemented using the Sieve of Eratosthenes algorithm.
"""

def calculate_primes(n):
    primes = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers