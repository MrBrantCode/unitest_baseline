"""
QUESTION:
Write a function, prime_numbers_in_range, that generates a list of all prime numbers within a given range from 2 to n (inclusive), where n is a positive integer. The function should return a list of integers.
"""

def prime_numbers_in_range(n):
    """
    Generates a list of all prime numbers within a given range from 2 to n (inclusive).

    Args:
        n (int): A positive integer.

    Returns:
        list: A list of integers representing prime numbers within the given range.
    """
    return [num for num in range(2, n+1) if all(num % i != 0 for i in range(2, int(num**0.5)+1))]