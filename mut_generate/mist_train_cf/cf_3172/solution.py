"""
QUESTION:
Write a function `calculate_series_stats` that takes a list of integers as input, where the length of the list is between 10 and 20 (inclusive), contains unique numbers, and is sorted in ascending order. The function should return the smallest number, largest number, and the average of the numbers in the list.
"""

def calculate_series_stats(series):
    """
    Calculate the smallest number, largest number, and the average of the numbers in the list.

    Args:
        series (list): A list of integers with unique numbers, sorted in ascending order.

    Returns:
        tuple: A tuple containing the smallest number, largest number, and the average of the numbers in the list.
    """
    smallest_num = series[0]
    largest_num = series[-1]
    avg_num = sum(series) / len(series)
    return smallest_num, largest_num, avg_num