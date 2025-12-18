"""
QUESTION:
Create a function `largest_prime_factor(n: int)` that returns the largest prime factor of a given integer `n`. The function should work with both positive and negative input values. Assume that the absolute value of `n` is greater than 1 and is not a prime number. Optimize the function to efficiently determine prime factors.
"""

def largest_prime_factor(n: int):
    n = abs(n)
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n