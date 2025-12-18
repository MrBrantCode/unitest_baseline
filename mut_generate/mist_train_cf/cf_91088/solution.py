"""
QUESTION:
Create a function called `reverse_list_copy` that creates a copy of the input list and reverses its elements without modifying the original list.
"""

def reverse_list_copy(input_list):
    """
    Creates a copy of the input list and reverses its elements without modifying the original list.

    Args:
        input_list (list): The original list to be copied and reversed.

    Returns:
        list: A reversed copy of the input list.
    """
    copied_list = input_list[:]
    copied_list.reverse()
    return copied_list