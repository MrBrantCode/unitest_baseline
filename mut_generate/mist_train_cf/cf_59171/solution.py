"""
QUESTION:
Write a function `sieve_of_eratosthenes(n)` that implements the Sieve of Eratosthenes algorithm to find all prime numbers less than a given number `n`. The function should return a list of prime numbers and have a time complexity of O(n log log n).
"""

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_nums = [p for p in range(2, n) if primes[p]]
    return prime_nums