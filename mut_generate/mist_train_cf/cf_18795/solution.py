"""
QUESTION:
Write a function named `sort_dict_reverse_alphabetical` that takes a dictionary as input and returns a new dictionary sorted in reverse alphabetical order by key. Assume all keys are strings and the dictionary is non-empty.
"""

def sort_dict_reverse_alphabetical(input_dict):
    """
    Returns a new dictionary sorted in reverse alphabetical order by key.

    Args:
        input_dict (dict): The dictionary to be sorted.

    Returns:
        dict: A new dictionary sorted in reverse alphabetical order by key.
    """
    return dict(sorted(input_dict.items(), key=lambda x: x[0], reverse=True))