"""
QUESTION:
Create a function `copy_dictionary` that takes a dictionary as input and returns a deep copy of the dictionary. The function should not modify the original dictionary.
"""

import copy

def copy_dictionary(input_dict):
    """
    Creates a deep copy of the input dictionary.

    Args:
        input_dict (dict): The dictionary to be copied.

    Returns:
        dict: A deep copy of the input dictionary.
    """
    return copy.deepcopy(input_dict)