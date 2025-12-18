"""
QUESTION:
Design a function `count_primes(n)` that counts the number of prime numbers less than a given integer `n`, where `n` is a positive integer greater than 1.
"""

def count_primes(n):
    sieve = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i: n: i] = [False] * len(sieve[i*i: n: i])
    return sum(sieve[2:])