"""
QUESTION:
Write a function named `is_equal` that takes two integer variables `x` and `y` as input, where `x` and `y` are bounded between 1 and a given integer `M`. Return 1 if `x` equals `y` and 0 otherwise. Note that the solution must be linear and feasible in the context of integer linear programming (ILP).
"""

def is_equal(x, y, M):
    """
    Checks if two integers x and y are equal within the bounds of 1 to M.

    Args:
    x (int): The first integer.
    y (int): The second integer.
    M (int): The upper bound for x and y.

    Returns:
    int: 1 if x equals y, 0 otherwise.
    """
    return 1 if x == y else 0