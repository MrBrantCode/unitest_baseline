"""
QUESTION:
Write a function named `sort_tuples` that takes a list of tuples as input, sorts them in ascending order based on the first element of each tuple, and returns the sorted list. The tuples can have up to 10 elements, each element can have up to 10 characters, and the list can contain up to 1 million tuples. The function should use a sorting algorithm with a time complexity of O(n log n) or better.
"""

def sort_tuples(tuples_list):
    """
    Sorts a list of tuples in ascending order based on the first element of each tuple.

    Args:
        tuples_list (list): A list of tuples to be sorted.

    Returns:
        list: The sorted list of tuples.
    """
    return sorted(tuples_list, key=lambda x: x[0])