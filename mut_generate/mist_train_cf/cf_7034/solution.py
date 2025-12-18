"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that uses the Sieve of Eratosthenes algorithm to find all prime numbers up to the given number `n`. The function should return a list of prime numbers from 2 to `n`.
"""

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for p in range(2, int(n**0.5) + 1):
        if primes[p] == True:
            for i in range(p*p, n+1, p):
                primes[i] = False

    return [i for i in range(2, n+1) if primes[i]]