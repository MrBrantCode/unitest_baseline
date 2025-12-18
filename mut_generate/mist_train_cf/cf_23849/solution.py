"""
QUESTION:
Write a function named `largest_prime_factor` that finds and returns the largest prime factor of a given integer `n`. The input `n` is an integer and the function should return an integer. The function should be efficient for large values of `n`.
"""

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n = n / i
        else:
            i += 1
    return n