"""
QUESTION:
Design a function `solve_linear_equation` that solves the linear equation `x + 2y = 4` for `x` when the value of `y` is given. The function should take `y` as input and return the corresponding value of `x`.
"""

def solve_linear_equation(y):
    """
    This function solves the linear equation x + 2y = 4 for x when the value of y is given.

    Args:
        y (int): The given value of y.

    Returns:
        int: The corresponding value of x.
    """
    x = 4 - 2*y
    return x