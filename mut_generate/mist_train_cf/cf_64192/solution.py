"""
QUESTION:
Create a function called `sieve_of_eratosthenes` that takes an integer `limit` as input and returns a list of all prime numbers up to `limit` using the Sieve of Eratosthenes algorithm. The function should be optimized for performance.
"""

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num*num, limit + 1, num):
                primes[multiple] = False
    return [i for i in range(2, limit + 1) if primes[i]]