"""
QUESTION:
Write a function `find_divisible_numbers` that takes a range of numbers from `start` to `end` (inclusive) and returns a list of numbers within this range that are divisible by both 3 and 5, but not by 7.
"""

def find_divisible_numbers(start, end):
    """
    Returns a list of numbers within the given range (inclusive) that are 
    divisible by both 3 and 5, but not by 7.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        list: A list of numbers that meet the divisibility criteria.
    """
    return [num for num in range(start, end + 1) if num % 3 == 0 and num % 5 == 0 and num % 7 != 0]