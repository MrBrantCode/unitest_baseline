"""
QUESTION:
Design a function called `sieve_of_eratosthenes(n)` that prints all prime numbers lower than or equal to a given number `n`. The function should take an integer `n` as input and return a list of prime numbers. Optimize the function to improve its efficiency and analyze its time complexity.
"""

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    
    prime_numbers = [p for p in range(2, n+1) if primes[p]]
    return prime_numbers