"""
QUESTION:
Given a list of prime numbers between 1000 and 10,000, write a function `next_primes(primes, n)` that generates the next `n` prime numbers in the sequence. The function should take two parameters: `primes`, a list of prime numbers, and `n`, the number of prime numbers to generate.
"""

import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def next_primes(primes, n):
    """Generate the next n prime numbers in the sequence."""
    start = primes[-1] + 1
    result = []
    while len(result) < n:
        if is_prime(start):
            result.append(start)
        start += 1
    return result