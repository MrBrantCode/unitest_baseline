"""
QUESTION:
Create a class with a method `calculate_primes` that takes an integer `n` as input and returns a list of prime numbers up to `n`. The method should handle edge cases such as negative input values and non-integer inputs, and it should be efficient for large input values. The input value `n` should be greater than or equal to 2.
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