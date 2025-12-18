"""
QUESTION:
Write a function `cubes_in_range` that calculates the cube of every integer in a given range, inclusively, and returns the result as a list. The function should take two parameters, `start` and `end`, representing the start and end of the range. The function should return a list of cubes of integers from `start` to `end`, inclusively.
"""

def cubes_in_range(start, end):
    """
    Calculate the cube of every integer in a given range, inclusively.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        list: A list of cubes of integers from start to end, inclusively.
    """
    return [i**3 for i in range(start, end + 1)]