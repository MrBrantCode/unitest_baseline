"""
QUESTION:
Create a function called `generate_odd_list` that generates a list of odd numbers within a specified range. The function should take two parameters, `start` and `end`, representing the range of numbers to consider. The function must be implemented recursively.
"""

def generate_odd_list(start, end):
    """
    Generates a list of odd numbers within a specified range recursively.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        list: A list of odd numbers within the specified range.
    """
    if start > end:
        return []
    elif start % 2 == 0:
        return generate_odd_list(start + 1, end)
    else:
        return [start] + generate_odd_list(start + 2, end)