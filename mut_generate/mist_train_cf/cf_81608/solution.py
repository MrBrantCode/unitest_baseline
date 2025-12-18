"""
QUESTION:
Implement a function `SieveOfEratosthenes(n)` to generate all prime numbers up to a given number `n` using the Sieve of Eratosthenes algorithm. The function should return a list of prime numbers.
"""

def SieveOfEratosthenes(n):
    """
    This function generates all prime numbers up to a given number `n` using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to `n`.
    """
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n+1) if primes[p]]
    return prime_numbers