"""
QUESTION:
Create a function `sieve_of_eratosthenes` that takes an integer `n` as input and returns a list of all prime numbers between 1 and `n`. The function should implement an optimization algorithm to reduce time complexity.
"""

def entrance(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers