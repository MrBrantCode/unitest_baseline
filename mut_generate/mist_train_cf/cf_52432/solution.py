"""
QUESTION:
Create a Python function `primes_in_range(start, end)` that returns a list of prime numbers in a given range from `start` to `end` (inclusive). The function should utilize a helper function `is_prime(n)` to check whether a number `n` is prime.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Return a list of prime numbers in a given range."""
    return [n for n in range(start, end+1) if is_prime(n)]