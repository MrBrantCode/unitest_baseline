"""
QUESTION:
Write a function, `find_divisible_sum`, that finds all numbers divisible by 3 and 5 but not a multiple of 7, within a given range. The function should return the sum of all such numbers found. The function should take two parameters: `start` and `end`, which represent the range of numbers to check. The range should be inclusive, meaning it includes both `start` and `end` values.
"""

def find_divisible_sum(start, end):
    """
    This function finds all numbers divisible by 3 and 5 but not a multiple of 7, 
    within a given range and returns the sum of all such numbers found.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        int: The sum of all numbers found.
    """
    return sum(num for num in range(start, end + 1) if num % 3 == 0 and num % 5 == 0 and num % 7 != 0)