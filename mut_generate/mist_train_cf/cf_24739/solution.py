"""
QUESTION:
Write a function `countOddNumbers` that takes two parameters, `start` and `end`, representing a range of integers. The function should return the count of all odd numbers within this range, inclusive. The range is defined as start ≤ i ≤ end.
"""

def countOddNumbers(start, end):
    """
    This function calculates the count of all odd numbers within a given range.

    Parameters:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).

    Returns:
    int: The count of all odd numbers within the range.
    """
    count = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            count += 1
    return count