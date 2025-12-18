"""
QUESTION:
Write a function named `sum_until_threshold` that calculates the sum of numbers from 0 up to a given threshold or 10, whichever comes first. The function should take one argument: `threshold`, an integer less than 10. It should return the sum of the numbers from 0 up to the threshold or 10.
"""

def sum_until_threshold(threshold: int) -> int:
    """
    Calculates the sum of numbers from 0 up to a given threshold or 10, whichever comes first.

    Args:
        threshold (int): An integer less than 10.

    Returns:
        int: The sum of the numbers from 0 up to the threshold or 10.
    """
    total = 0
    num = 0

    while num <= threshold and num <= 10:
        total += num
        num += 1

    return total