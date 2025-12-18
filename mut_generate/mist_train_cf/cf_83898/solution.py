"""
QUESTION:
Write a function `calculate_median` to calculate the median of a given list of numbers using the statistics library in Python. The function should take a list of numbers as input and return the calculated median.
"""

import statistics

def calculate_median(data):
    """
    Calculate the median of a given list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The calculated median.
    """
    return statistics.median(data)