"""
QUESTION:
Write a function named `generate_primes` that returns a list of all prime numbers between 1 and a given number `n` (inclusive). The function should only accept a positive integer as input.
"""

def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for x in range(2, int(n ** 0.5) + 1):
        if sieve[x]: 
            for i in range(x * x, n + 1, x): 
                sieve[i] = False
    for x in range(2, n + 1):
        if sieve[x]: 
            primes.append(x)
    return primes