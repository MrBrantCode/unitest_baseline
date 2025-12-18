"""
QUESTION:
Create a function called `sieve_of_eratosthenes(n)` that uses the Sieve of Eratosthenes algorithm to find all prime numbers up to the given number `n` and returns them as a list. The function should handle the case where `n` is a positive integer.
"""

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for p in range(2, int(n**0.5) + 1):
        if primes[p] == True:
            for i in range(p*p, n+1, p):
                primes[i] = False

    return [i for i in range(2, n+1) if primes[i]]