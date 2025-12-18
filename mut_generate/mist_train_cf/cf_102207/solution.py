"""
QUESTION:
Write a function `squares` that generates a list of squares of even numbers from 0 to n (inclusive) using list comprehension, where n is a given integer. The function should have a time complexity of O(n) and a potential memory usage of O(n).
"""

def squares(n):
    """
    Generates a list of squares of even numbers from 0 to n (inclusive) using list comprehension.

    Args:
    n (int): The upper limit (inclusive) for generating squares.

    Returns:
    list: A list of squares of even numbers from 0 to n (inclusive).
    """
    return [x**2 for x in range(n+1) if x % 2 == 0]