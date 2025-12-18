"""
QUESTION:
Write a function `calculate_y(x, z)` that takes two integers `x` and `z` as input and returns the value of `y` based on the following conditions:

- If `x` is greater than `z`, return `x + 19`.
- If `x` is less than or equal to `z`, return the maximum of `0` and `x - 20`.

Restrictions:
- The function should not use any loops (for or while).
- The function should handle the case where `x` is less than or equal to `0` and return `0` in that case.
"""

def calculate_y(x, z):
    """
    This function calculates the value of y based on the given conditions.

    Args:
        x (int): The first integer.
        z (int): The second integer.

    Returns:
        int: The calculated value of y.
    """

    if x > z:
        return x + 19
    else:
        return max(0, x - 20)