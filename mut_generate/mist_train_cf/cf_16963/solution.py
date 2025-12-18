"""
QUESTION:
Create a function `largest_prime_factor(n)` that finds and returns the largest prime factor of a given number `n`, where `n` can be up to 10^12. The function should only take one argument `n` and return the largest prime factor of `n`.
"""

import math

def largest_prime_factor(n):
    # Check if the number is divisible by 2
    while n % 2 == 0:
        largest_prime = 2
        n //= 2

    # Check for odd prime factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n //= i

    # If n is a prime number greater than 2
    if n > 2:
        largest_prime = n

    return largest_prime