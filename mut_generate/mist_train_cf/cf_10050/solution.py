"""
QUESTION:
Write a function `check_sum_range(num1, num2, start, end)` that checks if the sum of `num1` and `num2` is within the range `[start, end]` inclusive. The function should return `True` if the sum is within the range and `False` otherwise.
"""

def check_sum_range(num1, num2, start, end):
    """
    Checks if the sum of num1 and num2 is within the range [start, end] inclusive.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        bool: True if the sum is within the range, False otherwise.
    """
    return start <= num1 + num2 <= end