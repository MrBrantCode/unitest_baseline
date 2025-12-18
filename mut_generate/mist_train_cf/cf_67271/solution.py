"""
QUESTION:
Create a function `increment_list` that increments each element in the input list by 1 using list comprehension. The function should return the new list with the incremented elements. The original list should not be modified.
"""

def increment_list(input_list):
    """
    Increment each element in the input list by 1 using list comprehension.

    Args:
        input_list (list): The list to be incremented.

    Returns:
        list: A new list with the incremented elements.
    """
    return [x + 1 for x in input_list]