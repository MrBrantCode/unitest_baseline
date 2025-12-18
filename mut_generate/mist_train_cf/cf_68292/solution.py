"""
QUESTION:
Write a function named `find_max_value` that takes three numerical values as input and returns the maximum value among them. The function should not take any other parameters and should be able to handle any three numerical inputs.
"""

def find_max_value(a, b, c):
    """
    This function finds the maximum value among three numerical inputs.

    Args:
        a (int or float): The first numerical value.
        b (int or float): The second numerical value.
        c (int or float): The third numerical value.

    Returns:
        int or float: The maximum value among a, b, and c.
    """
    return max(a, b, c)