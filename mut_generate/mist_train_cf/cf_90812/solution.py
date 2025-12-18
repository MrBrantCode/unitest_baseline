"""
QUESTION:
Create a function `remove_duplicates` that takes a list of integers as input and returns a new list with no duplicate elements, while maintaining the original order of elements.
"""

def remove_duplicates(input_list):
    """
    This function takes a list of integers as input and returns a new list with no duplicate elements,
    while maintaining the original order of elements.

    Args:
        input_list (list): A list of integers.

    Returns:
        list: A new list with no duplicate elements.
    """
    new_list = []
    for num in input_list:
        if num not in new_list:
            new_list.append(num)
    return new_list