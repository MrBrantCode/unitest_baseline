"""
QUESTION:
Create a function `calculate_statistics` that takes a list of integers as input and returns the average, median, mode, range, and number of distinct elements in the list. The function should handle cases where the list has an odd or even number of elements. The mode should be the value that appears most frequently in the list, and if there are multiple modes, any one of them can be returned.
"""

from collections import Counter
import statistics

def calculate_statistics(data):
    """
    Calculate the average, median, mode, range, and number of distinct elements in a list of integers.

    Args:
    data (list): A list of integers.

    Returns:
    dict: A dictionary containing the average, median, mode, range, and number of distinct elements.
    """
    # Calculate average
    average = statistics.mean(data)

    # Calculate median
    median = statistics.median(data)

    # Calculate mode
    counter = Counter(data)
    mode = [k for k, v in counter.items() if v == max(counter.values())][0]

    # Calculate range
    range_data = max(data) - min(data)

    # Calculate number of distinct elements
    distinct_elements = len(set(data))

    return {
        "average": average,
        "median": median,
        "mode": mode,
        "range": range_data,
        "distinct_elements": distinct_elements
    }