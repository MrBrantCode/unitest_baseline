"""
QUESTION:
Write a function named `compute_expression` to calculate the value of the expression `(c^2 − b^2)^2 + a^2`. The function should take three parameters: `a`, `b`, and `c`.
"""

def compute_expression(a, b, c):
    """
    This function calculates the value of the expression (c^2 − b^2)^2 + a^2.

    Parameters:
    a (int): The first variable in the expression.
    b (int): The second variable in the expression.
    c (int): The third variable in the expression.

    Returns:
    int: The result of the expression.
    """
    return ((c**2 - b**2)**2 + a**2)