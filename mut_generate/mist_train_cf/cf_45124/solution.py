"""
QUESTION:
Write a function `count_primes(n)` that returns the count of all prime numbers from 1 to n (inclusive) using the Sieve of Eratosthenes algorithm. The function should return 0 if n is less than 2.
"""

def count_primes(n):
    if n < 2:
        return 0
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for current in range(2, int(n**0.5) + 1):
        if sieve[current]:
            for multiple in range(current*current, n + 1, current):
                sieve[multiple] = False
    return sum(sieve)