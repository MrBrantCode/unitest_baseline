"""
QUESTION:
Write a function `sort_tuples` that takes a list of tuples as input and returns the list sorted in ascending order by the first value of each tuple. The input list can contain up to 1 million tuples, and each tuple can have up to 10 elements with each element having up to 10 characters. The function should have a time complexity of O(n log n) or better.
"""

def sort_tuples(tuples_list):
    """
    Sorts a list of tuples in ascending order by the first value of each tuple.

    Args:
    tuples_list (list): A list of tuples.

    Returns:
    list: The sorted list of tuples.
    """
    return sorted(tuples_list, key=lambda x: x[0])