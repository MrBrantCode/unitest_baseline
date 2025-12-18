"""
QUESTION:
Create a Python function named `reverse_number` that takes an integer as input and returns the reversed integer using recursive programming. The function should handle integers of any number of digits.
"""

def reverse_integer(n):
    """
    Reverses an integer using recursive programming.

    Args:
    n (int): The input integer.

    Returns:
    int: The reversed integer.
    """
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        count_digits = len(str(remaining_digits))

        return last_digit * (10 ** count_digits) + reverse_integer(remaining_digits)