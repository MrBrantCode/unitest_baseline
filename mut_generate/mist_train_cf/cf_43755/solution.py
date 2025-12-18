"""
QUESTION:
Write a function named `calculate_median` to calculate the median of a given list of numbers. The function should first sort the numbers in ascending order, then find the middle value(s). If there is an odd number of observations, the middle number is the median. If there is an even number of observations, the median is the average of the two middle numbers.
"""

import statistics

def calculate_median(data):
    """
    Calculate the median of a given list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The median of the given list of numbers.
    """
    data.sort()
    return statistics.median(data)