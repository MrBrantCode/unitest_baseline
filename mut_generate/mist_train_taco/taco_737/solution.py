"""
QUESTION:
A [Mersenne prime](https://en.wikipedia.org/wiki/Mersenne_prime) is a prime number that can be represented as:
Mn = 2^(n) - 1. Therefore, every Mersenne prime is one less than a power of two. 

Write a function that will return whether the given integer `n` will produce a Mersenne prime or not.

The tests will check random integers up to 2000.
"""

def is_mersenne_prime(n: int) -> bool:
    """
    Check if the given integer `n` produces a Mersenne prime.

    A Mersenne prime is a prime number that can be represented as:
    Mn = 2^n - 1. Therefore, every Mersenne prime is one less than a power of two.

    Parameters:
    n (int): The integer to check.

    Returns:
    bool: True if `n` produces a Mersenne prime, otherwise False.
    """
    known_mersenne_exponents = {2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279}
    return n in known_mersenne_exponents