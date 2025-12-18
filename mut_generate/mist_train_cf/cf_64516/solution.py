"""
QUESTION:
Extract the second, third, and fourth elements from a given list.

Create a function named `get_middle_elements` that takes a list as an argument. The function should return a new list containing the second, third, and fourth elements of the input list, in the same order.
"""

def get_middle_elements(input_list):
    """
    Returns a new list containing the second, third, and fourth elements of the input list.

    Args:
    input_list (list): The input list from which elements are extracted.

    Returns:
    list: A new list containing the second, third, and fourth elements of the input list.
    """
    return input_list[1:4]