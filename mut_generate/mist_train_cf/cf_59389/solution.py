"""
QUESTION:
Write a function named `safe_division` that takes two integers `x` and `y` and returns the result of `x` divided by `y` using integer division. If `y` is zero, the function should handle the ZeroDivisionError and print an error message instead of crashing.
"""

def safe_division(x, y):
    """
    This function performs integer division of x by y and handles ZeroDivisionError.

    Args:
        x (int): The dividend.
        y (int): The divisor.

    Returns:
        int: The result of x divided by y if y is not zero.
    """
    try:
        return x // y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")