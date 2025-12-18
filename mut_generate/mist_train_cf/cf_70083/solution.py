"""
QUESTION:
Write a function `calculate_y` with two initial parameters `x` and `y`. The function should calculate a temporary variable `z` as the sum of `x` and `y`, then update `y` as the difference of `z` and `x`. The function should return the updated value of `y`.
"""

def calculate_y(x, y):
    """
    Calculate the updated value of y given x and initial y.

    Args:
    x (int): The first number
    y (int): The second number

    Returns:
    int: The updated value of y
    """
    z = x + y
    y = z - x
    return y