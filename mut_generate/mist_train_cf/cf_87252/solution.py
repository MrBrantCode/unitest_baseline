"""
QUESTION:
Create a function `insert_and_sort` that takes a list of integers `given_list` and an integer `new_element` as input. The function should return a new list that includes all elements from `given_list` and `new_element`, with `new_element` added to the end, and all elements sorted in ascending order.
"""

def insert_and_sort(given_list, new_element):
    """
    Inserts a new element into a given list and sorts the resulting list in ascending order.

    Args:
        given_list (list): A list of integers.
        new_element (int): The new integer to be inserted.

    Returns:
        list: A new list containing all elements from the given list and the new element, sorted in ascending order.
    """
    new_list = given_list + [new_element]
    new_list.sort()
    return new_list