"""
QUESTION:
Write a function `prime_numbers_at_multiple_of_3` that takes a list of integers as input and returns a list of prime numbers from the input list whose indices are multiples of 3.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_at_multiple_of_3(lst):
    """
    Returns a list of prime numbers from the input list whose indices are multiples of 3.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A list of prime numbers at indices that are multiples of 3.
    """
    return [num for i, num in enumerate(lst) if i % 3 == 0 and is_prime(num)]