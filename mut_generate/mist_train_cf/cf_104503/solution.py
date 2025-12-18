"""
QUESTION:
Write a function `divisible_sum` that finds all numbers divisible by 3 and 5 but not a multiple of 7, within a given range. The function should return the sum of these numbers. The range is defined by the parameters `start` and `end` (inclusive).
"""

def divisible_sum(start, end):
    """
    Finds all numbers divisible by 3 and 5 but not a multiple of 7, 
    within a given range and returns their sum.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        int: The sum of numbers divisible by 3 and 5 but not a multiple of 7.
    """
    return sum(num for num in range(start, end + 1) if num % 3 == 0 and num % 5 == 0 and num % 7 != 0)