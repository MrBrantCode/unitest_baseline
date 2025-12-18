"""
QUESTION:
Create a function `get_primes(n)` that generates an array of prime numbers within a specified numerical boundary `n`. The function should return all prime numbers from 2 up to, but not including, `n`.
"""

def get_primes(n):
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for i in range(x*x, n + 1, x):
                sieve[i] = False
    return [x for x in range(2, n) if sieve[x]]