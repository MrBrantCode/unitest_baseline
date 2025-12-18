"""
QUESTION:
Create a function named generate_positive_integers that generates a list containing all positive integers between 1 and a given number, n (inclusive).
"""

def generate_positive_integers(n):
    """
    Generates a list containing all positive integers between 1 and a given number, n (inclusive).

    Args:
        n (int): The upper limit (inclusive) for generating positive integers.

    Returns:
        list: A list of positive integers between 1 and n (inclusive).
    """
    return list(range(1, n + 1))