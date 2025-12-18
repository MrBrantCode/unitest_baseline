"""
QUESTION:
Create a function named `calculate_sum` that takes a list of integers as input and returns the sum of its elements without using any built-in sum functions or operators.
"""

def calculate_sum(lst):
    """
    Calculate the sum of a list of integers without using built-in sum functions or operators.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The sum of the elements in the list.
    """
    result = 0
    for num in lst:
        result += num
    return result