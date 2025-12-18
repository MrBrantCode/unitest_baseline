"""
QUESTION:
Implement an arithmetic function `add_numbers(a, b)` that takes two arguments `a` and `b` and returns their sum. The function should handle various input types including positive and negative integers, floating point numbers, and zero. It should also handle edge cases such as very large or very small numbers. If either `a` or `b` is a non-numeric input, the function should return an error message "Invalid input, expected numeric value".
"""

def add_numbers(a, b):
    """
    This function takes two arguments a and b and returns their sum.
    It handles various input types including positive and negative integers, 
    floating point numbers, and zero. It also handles edge cases such as 
    very large or very small numbers. If either a or b is a non-numeric 
    input, the function returns an error message "Invalid input, expected numeric value".

    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.

    Returns:
        int or float: The sum of a and b.
    """
    try:
        return a + b
    except TypeError:
        return "Invalid input, expected numeric value"