"""
QUESTION:
Write a function named `largest_prime_factor` that takes an integer `n` as input and returns the largest prime factor of `n`. The function should be efficient for large inputs.
"""

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n