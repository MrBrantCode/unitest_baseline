"""
QUESTION:
Create a function `find_intersection` that takes two lists of integers as input and returns a list of integers that exist in both input lists. The function should return a list, not a set, and the order of elements in the output list is not important. The function should be efficient for large input lists.
"""

def find_intersection(dataset_1, dataset_2):
    """
    Find the intersection of two lists of integers.

    Args:
        dataset_1 (list): The first list of integers.
        dataset_2 (list): The second list of integers.

    Returns:
        list: A list of integers that exist in both input lists.
    """
    return list(set(dataset_1) & set(dataset_2))