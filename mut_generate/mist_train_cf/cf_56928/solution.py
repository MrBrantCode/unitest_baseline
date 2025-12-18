"""
QUESTION:
Write a function named `is_prime` that determines whether a given number is prime, and use this function in a loop that runs from 10 down to 1 to print all prime numbers encountered. The `is_prime` function should be efficient and only check up to the square root of the number for factors.
"""

def is_prime(n):
    """Determine if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True