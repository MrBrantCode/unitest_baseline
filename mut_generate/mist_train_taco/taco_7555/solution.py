"""
QUESTION:
Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution. 

The inputs `x` and `y` are always greater or equal to 1, so the greatest common divisor will always be an integer that is also greater or equal to 1.
"""

def greatest_common_divisor(x: int, y: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two positive integers.

    Parameters:
    x (int): The first positive integer.
    y (int): The second positive integer.

    Returns:
    int: The greatest common divisor of x and y.
    """
    while y:
        x, y = y, x % y
    return x