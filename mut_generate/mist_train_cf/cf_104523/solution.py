"""
QUESTION:
Write a function `generate_primes` that generates a list of prime numbers within a given range using list comprehension. The range should be from 1 to `n`, where `n` is a positive integer. The function should only include prime numbers greater than 1 in the output list.
"""

def generate_primes(n):
    """
    Generates a list of prime numbers within a given range using list comprehension.

    Args:
        n (int): A positive integer representing the upper limit of the range.

    Returns:
        list: A list of prime numbers greater than 1 within the range from 1 to n.
    """
    return [x for x in range(2, n + 1) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]