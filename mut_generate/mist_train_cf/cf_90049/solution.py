"""
QUESTION:
Construct a function `iterate_even_numbers` that takes a list of integers as input and iterates through the list in reverse order, only considering even numbers. The function should terminate if it encounters a prime number and continue iterating only if the next element is a perfect square. The list contains at most 10^6 elements, and each element is a positive integer between 1 and 10^9 (inclusive).
"""

import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    """Check if a number is a perfect square."""
    return math.isqrt(n)**2 == n

def iterate_even_numbers(lst):
    """Iterate through a list in reverse order, only considering even numbers.
    Terminate if a prime number is encountered and continue iterating only if the next element is a perfect square.

    Args:
        lst (list): A list of integers.

    Returns:
        None
    """
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 2 == 0:
            if is_prime(lst[i]):
                break
            if i > 0 and is_perfect_square(lst[i - 1]):
                print(lst[i])