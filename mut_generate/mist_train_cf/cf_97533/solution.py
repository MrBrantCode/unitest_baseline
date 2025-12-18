"""
QUESTION:
Write a function named 'multiply' that takes two arguments: an integer 'x' and a list of integers 'y', and returns a list of integers that are the result of multiplying 'x' with each element in 'y'. The function should use list comprehension.
"""

def multiply(x, y):
    """
    Returns a list of integers that are the result of multiplying 'x' with each element in 'y'.

    Args:
        x (int): The multiplier.
        y (list): A list of integers to be multiplied.

    Returns:
        list: A list of integers.
    """
    return [x * i for i in y]