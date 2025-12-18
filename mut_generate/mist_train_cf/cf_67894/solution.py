"""
QUESTION:
Create a function `sieve_of_eratosthenes(limit)` that returns a list of all prime numbers up to the given limit. The function should use the Sieve of Eratosthenes algorithm and only include numbers that are actually prime.
"""

def sieve_of_eratosthenes(limit):
    """
    Returns a list of all prime numbers up to the given limit using the Sieve of Eratosthenes algorithm.

    Args:
        limit (int): The upper limit for finding prime numbers.

    Returns:
        list: A list of prime numbers up to the given limit.
    """
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    prime_nums = [p for p in range(2, limit + 1) if primes[p]]
    return prime_nums