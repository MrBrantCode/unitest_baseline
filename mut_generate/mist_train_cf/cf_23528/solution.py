"""
QUESTION:
Write a Python function `calculate_y` that takes an integer `x` as input and returns the corresponding `y` value based on the following conditions: if `x` equals 1, `y` is 10; if `x` equals 2, `y` is 20; if `x` equals 3, `y` is 30. Implement this logic using a switch statement or the equivalent Python syntax. The function should not handle cases where `x` is not 1, 2, or 3.
"""

def calculate_y(x):
    """
    Calculate the corresponding y value for a given x.

    Args:
        x (int): The input value.

    Returns:
        int: The corresponding y value.
    """
    return {1: 10, 2: 20, 3: 30}.get(x)