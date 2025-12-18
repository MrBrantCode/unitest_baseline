"""
QUESTION:
Write a function `sort_fruit_occurrences` that takes a list of tuples as input, where each tuple contains an integer and a string. Sort the list in descending order of the occurrence of the string (the second element of each tuple). If two or more tuples have the same string, sort them by the string itself in ascending order.
"""

from collections import Counter

def sort_fruit_occurrences(lst):
    """
    Sorts a list of tuples in descending order of the occurrence of the string (the second element of each tuple).
    If two or more tuples have the same string, sorts them by the string itself in ascending order.

    Args:
        lst (list): A list of tuples, where each tuple contains an integer and a string.

    Returns:
        list: The sorted list of tuples.
    """
    counter = Counter(x[1] for x in lst)
    return sorted(lst, key=lambda x: (-counter[x[1]], x[1]))