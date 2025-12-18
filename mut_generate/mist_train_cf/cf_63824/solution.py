"""
QUESTION:
Write a function named `is_perfect_square_or_cube` that determines if any numbers in a given list of integers are perfect cubes or perfect squares. The function should return a string indicating whether each number is a perfect square or cube, or neither. The function should use the `round()` function to correctly identify perfect squares and cubes.
"""

def is_perfect_square_or_cube(num):
    """
    Determines if a number is a perfect square, perfect cube, or neither.

    Args:
        num (int): The number to check.

    Returns:
        str: A string indicating whether the number is a perfect square, perfect cube, or neither.
    """
    if round(num ** (1/3)) ** 3 == num:
        return f"{num} is a perfect cube."
    elif round(num ** (1/2)) ** 2 == num:
        return f"{num} is a perfect square."
    else:
        return f"{num} is neither a perfect square nor a cube."