"""
QUESTION:
Create a function named `get_integers` that takes two parameters, `start` and `end`, and returns a list of integers between `start` and `end` (inclusive of `end`), excluding any numbers that are divisible by 3.
"""

def get_integers(start, end):
    """
    Returns a list of integers between start and end (inclusive of end), 
    excluding any numbers that are divisible by 3.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        list: A list of integers between start and end, excluding any numbers that are divisible by 3.
    """
    return [x for x in range(start, end+1) if x % 3 != 0]