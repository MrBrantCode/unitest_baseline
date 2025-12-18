"""
QUESTION:
Write a function called `sort_dict_by_value` that takes a dictionary as an input, sorts its items based on the ascending order of its values, and returns the sorted dictionary. The function should work for Python versions 3.7 and above.
"""

def sort_dict_by_value(input_dict):
    """
    This function sorts the input dictionary by its values in ascending order.
    
    Args:
        input_dict (dict): The dictionary to be sorted.
    
    Returns:
        dict: The sorted dictionary.
    """
    return dict(sorted(input_dict.items(), key=lambda item: item[1]))