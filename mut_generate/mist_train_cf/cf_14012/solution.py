"""
QUESTION:
Implement a function `sieve_of_eratosthenes(n)` that generates an array of all prime numbers between 1 and `n` (inclusive) using the Sieve of Eratosthenes algorithm. The function should return the array of prime numbers. The input `n` is an integer.
"""

def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(n**0.5) + 1):
        if sieve[p] is True:
            for i in range(p**2, n + 1, p):
                sieve[i] = False

    for p in range(2, n + 1):
        if sieve[p] is True:
            primes.append(p)

    return primes