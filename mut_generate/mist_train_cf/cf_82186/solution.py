"""
QUESTION:
Create a function named `is_prime(n)` that checks whether a given number `n` is prime or not. Use this function to print all prime numbers between 20 and 80.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True