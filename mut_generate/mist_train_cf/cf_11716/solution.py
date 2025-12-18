"""
QUESTION:
Write a function called `calculate_remainder` that takes two positive integers `num1` and `num2` as input. The function should return the remainder of `num1` divided by `num2`. However, if `num2` is equal to zero, it should return an error message "Error: Division by zero is not possible".
"""

def calculate_remainder(num1, num2):
    """
    Calculate the remainder of num1 divided by num2.

    Args:
        num1 (int): The dividend.
        num2 (int): The divisor.

    Returns:
        int: The remainder of num1 divided by num2, or an error message if num2 is zero.
    """
    if num2 == 0:
        return "Error: Division by zero is not possible"
    return num1 % num2