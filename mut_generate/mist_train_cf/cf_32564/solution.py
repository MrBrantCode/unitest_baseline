"""
QUESTION:
Implement a function `calculate_result` that takes in an object containing four values: x, y, s, t, and a boolean flag `val`. If `val` is True, the function should return the result of the calculation `(x * y) + (s - t)`. If `val` is False, the function should return the result of the calculation `(x + y) * (s - t)`.
"""

def calculate_result(x, y, s, t, val):
    """
    Calculates the result based on the provided values and a boolean flag.

    If val is True, returns (x * y) + (s - t).
    If val is False, returns (x + y) * (s - t).

    Args:
        x (int): The value of x.
        y (int): The value of y.
        s (int): The value of s.
        t (int): The value of t.
        val (bool): The boolean flag.

    Returns:
        int: The calculated result.
    """
    if val:
        return (x * y) + (s - t)
    else:
        return (x + y) * (s - t)