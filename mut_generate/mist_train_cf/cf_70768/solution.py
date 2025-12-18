"""
QUESTION:
Implement a function named `prime_sieve(n)` that generates and returns a list of all prime numbers less than or equal to `n`, where `n` is a given number. The function should be optimized for efficiency and have a time complexity of O(n log log n).
"""

def prime_sieve(n):
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for i in range(x*x, n + 1, x):
                sieve[i] = False
    return [x for x in range(2, n+1) if sieve[x]]