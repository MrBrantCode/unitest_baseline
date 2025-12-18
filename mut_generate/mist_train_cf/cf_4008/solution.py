"""
QUESTION:
Write a function `sort_dict_reverse_alpha` that takes a dictionary as input and returns a new dictionary with its keys sorted in reverse alphabetical order, ignoring case sensitivity. The function should not modify the original dictionary.
"""

def sort_dict_reverse_alpha(input_dict):
    """
    Returns a new dictionary with its keys sorted in reverse alphabetical order, 
    ignoring case sensitivity.

    Args:
    input_dict (dict): The dictionary to be sorted.

    Returns:
    dict: A new dictionary with its keys sorted in reverse alphabetical order.
    """
    return dict(sorted(input_dict.items(), key=lambda x: x[0].lower(), reverse=True))