"""
QUESTION:
Write a function `calculate_average` that takes four integers as inputs: two integers `int1` and `int2`, and a range defined by `range_start` and `range_end` (inclusive). The function should calculate the average of all integers within the given range, excluding `int1` and `int2`. If no integers are within the range (excluding `int1` and `int2`), the function should return 0.
"""

def calculate_average(int1, int2, range_start, range_end):
    """
    Calculate the average of all integers within a given range, excluding two specified integers.

    Args:
    int1 (int): The first integer to exclude.
    int2 (int): The second integer to exclude.
    range_start (int): The start of the range (inclusive).
    range_end (int): The end of the range (inclusive).

    Returns:
    float: The average of the integers in the range, excluding int1 and int2. If no integers are within the range, returns 0.
    """
    total = sum(num for num in range(range_start, range_end+1) if num not in (int1, int2))
    count = sum(1 for num in range(range_start, range_end+1) if num not in (int1, int2))

    return total / count if count != 0 else 0