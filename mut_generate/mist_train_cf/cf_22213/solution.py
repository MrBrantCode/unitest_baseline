"""
QUESTION:
Implement a function called process_list that takes a list of integers as input and returns a new list. For each element in the input list, if the index of the element is even, the corresponding element in the output list should be the element's value plus 1. If the index is odd, the corresponding element in the output list should be the element's value minus 1.
"""

def process_list(input_list):
    """
    This function processes a list of integers by adding 1 to the elements at even indices 
    and subtracting 1 from the elements at odd indices.

    Args:
        input_list (list): A list of integers.

    Returns:
        list: A new list with the elements modified according to the index.
    """
    return [x + 1 if i % 2 == 0 else x - 1 for i, x in enumerate(input_list)]