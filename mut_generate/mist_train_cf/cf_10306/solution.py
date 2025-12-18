"""
QUESTION:
Write a function called `largest_prime_factor` that takes an integer as input and returns the largest prime factor of that integer. The function should handle integers greater than 1.
"""

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    if n > 1:
        return n
    return i