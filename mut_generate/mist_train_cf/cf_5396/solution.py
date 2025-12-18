"""
QUESTION:
Create a function named `find_primes` that takes an integer `n` as input and returns a list of prime numbers less than `n`. The function should raise a custom exception if the input `n` is not a positive integer greater than 1. The function should have a time complexity of O(n^1.5) or better and a space complexity of O(n).
"""

class InvalidInputException(Exception):
    pass


def find_primes(n):
    """
    Returns a list of prime numbers less than n.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        list: A list of prime numbers less than n.

    Raises:
        InvalidInputException: If n is not a positive integer greater than 1.
    """
    if not isinstance(n, int) or n <= 1:
        raise InvalidInputException("Input must be a positive integer greater than 1.")
    primes = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes