"""
QUESTION:
Generate a sequence of n prime numbers using the Sieve of Eratosthenes method. The function should be named `sieve_of_eratosthenes(n)`. The function should return the first n prime numbers.
"""

def sieve_of_eratosthenes(n):
    limit = 1000  # Assume the nth prime number is less than this limit
    sieve = [True] * limit  # Initially assume all numbers are prime
    sieve[0] = sieve[1] = False
    for ind, val in enumerate(sieve):
        if val is True:
            sieve[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
    primes = [i for i, val in enumerate(sieve) if val is True]
    return primes[:n]