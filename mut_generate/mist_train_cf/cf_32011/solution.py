"""
QUESTION:
Implement a function `sieve_of_eratosthenes` in a Python module that takes an integer `limit` as input and returns a list of all prime numbers up to the given limit using the Sieve of Eratosthenes algorithm. The function should be optimized for performance using Cython and should be compilable into a C extension module. The input limit is an integer greater than 1, and the output should be a list of integers.
"""

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(limit + 1) if primes[i]]