"""
QUESTION:
Implement a function named `sum_of_primes(n)` that takes an integer `n` as input and returns the sum of all prime numbers up to `n` (inclusive) using the Sieve of Eratosthenes algorithm. The function should handle edge cases where `n` is not a positive integer greater than 1.
"""

def sum_of_primes(n):
    def sieve_of_eratosthenes(n):
        primes = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (primes[p] == True):
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return primes

    primes = sieve_of_eratosthenes(n)
    prime_nums = [p for p in range(2, n+1) if primes[p]]
    return sum(prime_nums)