"""
QUESTION:
Write a function `check_sorted_options(options)` that takes a dictionary `options` where keys are option letters and values are lists of integers. The function should return the key(s) of the option(s) where the list of integers is already sorted in ascending order.
"""

def check_sorted_options(options):
    """
    Returns the key(s) of the option(s) where the list of integers is already sorted in ascending order.

    Args:
        options (dict): A dictionary where keys are option letters and values are lists of integers.

    Returns:
        list: A list of keys where the corresponding list of integers is sorted in ascending order.
    """
    return [key for key in options if options[key] == sorted(options[key])]