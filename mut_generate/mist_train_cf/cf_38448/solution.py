"""
QUESTION:
Write a Python function `sum_of_multiples_of_3(start, end)` that calculates the sum of all numbers that are multiples of 3 within a given inclusive range. The function should take two integer parameters, `start` and `end`, representing the range of numbers to consider, and return the sum of all numbers within this range that are multiples of 3.
"""

def sum_of_multiples_of_3(start, end):
    """
    Calculate the sum of all numbers that are multiples of 3 within a given inclusive range.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        int: The sum of all numbers within the range that are multiples of 3.
    """
    return sum(i for i in range(start, end + 1) if i % 3 == 0)