"""
QUESTION:
Create a function `five_nine_twelve(n)` that calculates and returns the sum of all numbers less than `n` that contain the digit 5 and are divisible by either 9 or 12 without leaving a remainder.
"""

def five_nine_twelve(n: int) -> int:
    """
    This function calculates the sum of all numbers less than `n` that contain the digit 5 and are divisible by either 9 or 12 without leaving a remainder.

    Args:
        n (int): The upper limit of the range of numbers to consider.

    Returns:
        int: The sum of all numbers less than `n` that meet the given conditions.
    """
    total = 0
    for i in range(1, n):
        if '5' in str(i) and (i % 9 == 0 or i % 12 == 0):
            total += i
    return total