"""
QUESTION:
Write a function `count_integers_in_range` that takes two parameters, `start` and `end`, representing the start and end of a range (inclusive). The function should return the total number of integers within this range.
"""

def count_integers_in_range(start, end):
    """
    This function calculates the total number of integers within a given range (inclusive).
    
    Parameters:
    start (int): The start of the range.
    end (int): The end of the range.
    
    Returns:
    int: The total number of integers within the range.
    """
    return end - start + 1