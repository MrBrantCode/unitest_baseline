"""
QUESTION:
Write a function `find_minimum` that takes three integers `num1`, `num2`, and `num3` as input and returns the smallest of the three. The function should handle integers in the range of -1000 to 1000.
"""

def find_minimum(num1, num2, num3):
    """
    Returns the smallest of three integers.

    Args:
    num1 (int): The first integer.
    num2 (int): The second integer.
    num3 (int): The third integer.

    Returns:
    int: The smallest of the three integers.
    """
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3