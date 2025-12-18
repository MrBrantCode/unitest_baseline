"""
QUESTION:
Create a function named `largest_prime_factor` that takes a positive integer `n` as input and returns the largest prime factor of `n` that is greater than 1,000.
"""

import math

def largest_prime_factor(n):
    # Divide by 2 until it is no longer divisible
    while n % 2 == 0:
        n //= 2

    # Check odd numbers up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i

    # If n is still greater than 2, it is a prime factor
    if n > 2:
        return n
    else:
        return None