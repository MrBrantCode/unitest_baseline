"""
QUESTION:
Write a function `largest_prime_factor(n)` that returns the largest prime factor of an integer `n`, where `n` can be either positive or negative, `n` is greater than 1 in absolute value, and `n` is not a prime number.
"""

def largest_prime_factor(n: int):
    n = abs(n)  # ensures we also cover negative input
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n