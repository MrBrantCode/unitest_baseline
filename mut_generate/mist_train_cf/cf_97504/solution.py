"""
QUESTION:
Write a function called `generate_quadratic_pattern` that generates the first n terms of a quadratic pattern represented by the polynomial equation n^2 + n + 1, starting from n=0. The function should return a list of integers representing the quadratic pattern.
"""

def generate_quadratic_pattern(n):
    """
    Generates the first n terms of a quadratic pattern represented by the polynomial equation n^2 + n + 1.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: A list of integers representing the quadratic pattern.
    """
    return [i**2 + i + 1 for i in range(n)]