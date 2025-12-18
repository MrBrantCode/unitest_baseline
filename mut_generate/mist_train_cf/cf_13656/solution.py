"""
QUESTION:
Create a class with a method named `calculate_primes` that takes an integer `n` as input, where `n` is greater than or equal to 2, and returns a list of prime numbers up to `n`. The method should handle non-integer and negative input values, and be efficient enough to handle large input values.
"""

def calculate_primes(n):
    if not isinstance(n, int) or n < 2:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [i for i in range(2, n + 1) if primes[i]]