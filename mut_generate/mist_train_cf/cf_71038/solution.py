"""
QUESTION:
Write a function `sort_tuples_by_second_element` that sorts a list of tuples in ascending order based on their second elements. The input list will contain tuples with two elements each, and the function should return the sorted list of tuples.
"""

def sort_tuples_by_second_element(tuples):
    """
    Sorts a list of tuples in ascending order based on their second elements.

    Args:
    tuples (list): A list of tuples with two elements each.

    Returns:
    list: The sorted list of tuples.
    """
    return sorted(tuples, key=lambda x: x[1])