"""
QUESTION:
Create a function named `sort_and_reverse_tuples` that takes a list of tuples as input. The function should sort the list of tuples based on the third element of each tuple in descending order, and for tuples with the same third element, they should be sorted based on the second element in ascending order. The function should be able to handle tuples with floating point numbers as the third element.
"""

def sort_and_reverse_tuples(list_of_tuples):
    """
    Sorts a list of tuples based on the third element in descending order.
    For tuples with the same third element, they are sorted based on the second element in ascending order.

    Args:
        list_of_tuples (list): A list of tuples.

    Returns:
        list: A sorted list of tuples.
    """
    sorted_list = sorted(list_of_tuples, key=lambda tup: (-tup[2], tup[1]))
    return sorted_list