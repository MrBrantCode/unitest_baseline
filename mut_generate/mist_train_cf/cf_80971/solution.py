"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a prime number. Use this function to generate an array of prime numbers between 500 and 1000 (inclusive) and return this array.
"""

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True