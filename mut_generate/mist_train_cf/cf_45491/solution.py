"""
QUESTION:
Write a function `largest_prime_factor(n)` that finds the largest prime number that evenly divides the given number `n`. The function should only take an integer `n` as input and return the largest prime factor.
"""

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n