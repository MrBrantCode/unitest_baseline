"""
QUESTION:
Write a function `sieve_of_eratosthenes` that takes an integer `n` as input and returns a list of all prime numbers less than or equal to `n`. Use a boolean list where initially all values are set to `True` except for the indices 0 and 1, which should be set to `False`, to mark non-prime numbers. The function should implement the Sieve of Eratosthenes algorithm.
"""

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime

    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    primes = [i for i in range(2, n + 1) if sieve[i]]
    return primes