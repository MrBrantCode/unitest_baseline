"""
QUESTION:
Write a function `generate_quadratic_pattern` that generates the first n terms of a quadratic pattern represented by the polynomial equation n^2 + n + 1, starting from n=0. The function should take one integer parameter `n` and return a list of the first n terms of the pattern.
"""

def generate_quadratic_pattern(n):
    """
    Generates the first n terms of a quadratic pattern represented by the polynomial equation n^2 + n + 1, starting from n=0.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: A list of the first n terms of the pattern.
    """
    return [i**2 + i + 1 for i in range(n)]