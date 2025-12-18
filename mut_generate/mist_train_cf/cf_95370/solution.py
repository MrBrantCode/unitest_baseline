"""
QUESTION:
Create a function called `sort_dict_reverse_alphabetical` that sorts a given dictionary of strings by its keys in reverse alphabetical order. The input dictionary should be a dictionary where keys and values are both strings. The function should return a new dictionary with the same keys and values as the input dictionary, but sorted by key in reverse alphabetical order.
"""

def sort_dict_reverse_alphabetical(input_dict):
    """
    Sorts a dictionary of strings by its keys in reverse alphabetical order.

    Args:
        input_dict (dict): A dictionary where keys and values are both strings.

    Returns:
        dict: A new dictionary with the same keys and values as the input dictionary, 
              but sorted by key in reverse alphabetical order.
    """
    return dict(sorted(input_dict.items(), key=lambda x: x[0], reverse=True))