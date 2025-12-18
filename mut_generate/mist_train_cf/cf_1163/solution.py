"""
QUESTION:
Create a function `custom_sort` that takes a list of unique integers as input and returns the list sorted in descending order using a custom sorting algorithm (not the built-in sorting function). The input list will contain 10 unique random integers between 1 and 1000.
"""

def custom_sort(series):
    """
    Sorts a list of unique integers in descending order using a custom sorting algorithm.

    Args:
        series (list): A list of unique integers.

    Returns:
        list: The sorted list in descending order.
    """
    n = len(series)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if series[j] < series[j + 1]:
                series[j], series[j + 1] = series[j + 1], series[j]
    return series