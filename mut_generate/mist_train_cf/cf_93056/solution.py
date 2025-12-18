"""
QUESTION:
Implement a function called `sieve_of_eratosthenes` that takes an integer `n` as input and returns a list of all prime numbers between 1 and `n` (inclusive) using the Sieve of Eratosthenes algorithm. The function should use a boolean array (or equivalent data structure) to mark off composite numbers and return the remaining prime numbers. The input `n` is a positive integer.
"""

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(n**0.5) + 1):
        if sieve[p] is True:
            for i in range(p**2, n + 1, p):
                sieve[i] = False

    return [p for p in range(2, n + 1) if sieve[p] is True]