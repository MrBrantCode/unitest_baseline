"""
QUESTION:
Write a function named `is_prime` that checks if a given integer `n` is a prime number and returns a boolean value. The function should be able to handle integers greater than 1.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return False