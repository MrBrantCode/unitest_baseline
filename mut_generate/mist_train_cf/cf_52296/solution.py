"""
QUESTION:
Implement a custom generator function `even_primes` that generates even prime numbers within a given range `n`. The function should use the `yield` keyword to produce a sequence of even prime numbers and should utilize a helper function `is_prime` to determine if a number is prime.
"""

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def even_primes(n):
    """
    Custom generator function to generate even prime numbers within a given range n.

    Args:
    n (int): The upper limit of the range.

    Yields:
    int: Even prime numbers within the range.
    """
    for i in range(n):
        if i % 2 == 0 and is_prime(i):
            yield i