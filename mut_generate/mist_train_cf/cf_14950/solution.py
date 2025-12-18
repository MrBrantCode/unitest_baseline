"""
QUESTION:
Write a function `bitwise_assign(x, y)` that takes two integers `x` and `y` as input and returns the value of `y` after assigning the value of `x` to `y` using only bitwise operators. The function should not use assignment operators (=), if-else statements, or any other operators that can directly assign the value of `x` to `y`.
"""

def bitwise_assign(x, y):
    """
    Assign the value of x to y using only bitwise operators.

    Args:
        x (int): The value to be assigned.
        y (int): The value to be overwritten.

    Returns:
        int: The value of y after assignment.
    """
    return x | (~y & x) 