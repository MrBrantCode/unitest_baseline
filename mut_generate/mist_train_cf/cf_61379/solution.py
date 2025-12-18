"""
QUESTION:
Write a function `calculate_median` that takes a list of salaries as input and returns the median salary. The function should use the `statistics.median` function from Python's built-in statistics module to calculate the median. The input list may contain a mix of integers and/or floats representing salaries. The function should not take any additional arguments.
"""

import statistics

def calculate_median(salaries):
    """
    Calculate the median salary from a list of salaries.

    Args:
        salaries (list): A list of salaries.

    Returns:
        float: The median salary.
    """
    return statistics.median(salaries)