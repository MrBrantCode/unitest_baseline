"""
QUESTION:
Create a function named `list_stats` that takes a list of integers as input and returns a string containing the mean, median, and mode of the list. The function should handle exceptions for an empty list and non-integer values within the list, and it should be optimized for large lists.
"""

from collections import Counter
import statistics as stats

def list_stats(lst):
    """This function returns the mean, median and mode of a list of integers."""
    try:
        if not lst:  # check if list is empty
            return 'The list is empty.'
        elif not all(isinstance(i, int) for i in lst):  # check if all elements are integers
            return 'The list should only contain integers.'
        else:
            return 'Mean: {}, Median: {}, Mode: {}'.format(stats.mean(lst),
                                                          stats.median(lst),
                                                          stats.mode(lst))

    except Exception as e:
        return str(e)