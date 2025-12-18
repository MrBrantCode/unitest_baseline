"""
QUESTION:
Write a function `generate_primes(n)` that generates prime numbers up to a given number `n` using the Sieve of Eratosthenes algorithm. The function should return a list of prime numbers. The input `n` is an integer, and the output is a list of integers. The function should handle edge cases where `n` is less than or equal to 1.
"""

def generate_primes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers