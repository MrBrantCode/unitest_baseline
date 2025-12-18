"""
QUESTION:
Write a function `filter_numbers` that takes a list of integers and two numbers `X` and `Y` as input. Return a list of numbers from the original list that are greater than `X` and less than or equal to `Y`.
"""

def filter_numbers(lst, X, Y):
    """
    Filters a list of numbers to include only those greater than X and less than or equal to Y.

    Args:
        lst (list): A list of integers.
        X (int): The lower bound (exclusive).
        Y (int): The upper bound (inclusive).

    Returns:
        list: A list of integers that meet the specified conditions.
    """
    return [num for num in lst if num > X and num <= Y]