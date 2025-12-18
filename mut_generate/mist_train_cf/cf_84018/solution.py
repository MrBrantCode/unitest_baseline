"""
QUESTION:
Create a function named 'primes' that prints a list of all the prime numbers from a given list of integers. The function should be able to handle massive lists (in terms of millions of elements) without crashing due to memory limitations.
"""

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_factor = round(n**0.5)
    for factor in range(3, max_factor+1, 2):
        if n % factor == 0:
            return False
    return True

def primes(numbers):
    """Generator function to yield prime numbers from a given list."""
    for num in numbers:
        if is_prime(num):
            yield num