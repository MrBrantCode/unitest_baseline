"""
QUESTION:
Write a function `sum_of_natural_numbers(n)` that calculates the sum of the first n natural numbers with a time complexity of O(1). The function should accept an integer `n` as input, return an error message if `n` is not an integer, and return an error message if `n` is a negative value.
"""

def sum_of_natural_numbers(n):
    """
    Calculates the sum of the first n natural numbers with a time complexity of O(1).

    Args:
        n (int): The number of natural numbers to sum.

    Returns:
        int: The sum of the first n natural numbers, or an error message if n is not an integer or is negative.
    """
    if not isinstance(n, int):
        return "Error: n is not an integer."
    elif n < 0:
        return "Error: n is a negative value."
    else:
        return (n * (n + 1)) // 2