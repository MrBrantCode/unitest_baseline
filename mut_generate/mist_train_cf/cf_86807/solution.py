"""
QUESTION:
Generate a function `custom_sort` that sorts a list of unique integers in descending order using a custom implementation of a sorting algorithm, without using the built-in sorting function of the programming language. The function should take a list of integers as input and return the sorted list.
"""

def custom_sort(series):
    """
    Sorts a list of unique integers in descending order using a custom implementation of a sorting algorithm.

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