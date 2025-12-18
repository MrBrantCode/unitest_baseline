"""
QUESTION:
Write a function `invert_dictionary` that takes a dictionary as input and returns a new dictionary where the keys and values are swapped. The input dictionary is guaranteed to have unique and hashable values. If the input dictionary has duplicate values, the resulting dictionary should contain the last key-value pair for each duplicate value.
"""

def invert_dictionary(dictionary):
    """
    Inverts the keys and values of a dictionary.
    
    Args:
        dictionary (dict): The dictionary to be inverted.
    
    Returns:
        dict: A new dictionary where the keys and values are swapped.
    """
    return {v: k for k, v in dictionary.items()}