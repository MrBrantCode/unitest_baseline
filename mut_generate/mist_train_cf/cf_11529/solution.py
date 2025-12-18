"""
QUESTION:
Create a function `remove_duplicates` that takes a list of elements as input and returns a new list containing the same elements but with duplicates removed. The function should not use any built-in Python functions or data structures that can remove duplicates, such as set or dict. The order of elements in the original list should be preserved in the output list.
"""

def remove_duplicates(input_list):
    """
    This function takes a list of elements as input, removes duplicates, 
    and returns a new list while preserving the original order.

    Args:
        input_list (list): A list of elements

    Returns:
        list: A new list containing the same elements but with duplicates removed
    """
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements