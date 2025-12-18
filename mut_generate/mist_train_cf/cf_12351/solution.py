"""
QUESTION:
Write a function called `add_values` that takes two parameters, `x` and `y`, and returns their sum. The function should work with the given code: `x = 10`, `y = "10"`, and `z = add_values(x, y)`. The function must handle data type conversion to perform the addition operation.
"""

def add_values(x, y):
    """
    This function adds two values together. It handles data type conversion 
    to perform the addition operation if one of the parameters is a string.

    Parameters:
    x (int): The first number to add.
    y (int or str): The second number to add.

    Returns:
    int: The sum of x and y.
    """
    return x + int(y)