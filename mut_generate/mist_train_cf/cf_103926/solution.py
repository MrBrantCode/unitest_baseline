"""
QUESTION:
Write a function named `sort_tuples_by_second_element` that takes a list of tuples as input and returns the list sorted in descending order based on the second element of each tuple.
"""

def sort_tuples_by_second_element(tuples_list):
    """
    Sorts a list of tuples in descending order based on the second element of each tuple.

    Args:
        tuples_list (list): A list of tuples.

    Returns:
        list: The sorted list of tuples.
    """
    return sorted(tuples_list, key=lambda x: x[1], reverse=True)