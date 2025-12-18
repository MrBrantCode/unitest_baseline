"""
QUESTION:
Create a function named "func" that calculates the sum of all non-negative integers from 0 to the given input "n" (inclusive) and returns the result. If the input "n" is a negative number, return the error message "Input must be a non-negative integer."
"""

def func(n):
    """
    This function calculates the sum of all non-negative integers from 0 to the given input "n" (inclusive) and returns the result.
    If the input "n" is a negative number, return the error message "Input must be a non-negative integer."

    Args:
        n (int): The input number up to which the sum is calculated.

    Returns:
        int or str: The sum of integers from 0 to n if n is non-negative, otherwise an error message.
    """
    if n == 0:
        return 0
    elif n < 0:
        return "Input must be a non-negative integer."
    else:
        return n + func(n - 1)