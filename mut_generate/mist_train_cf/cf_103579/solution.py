"""
QUESTION:
Create a function `name_lengths(names)` that takes a list of names as input and returns a new list containing the lengths of each name in the original list. Each name must be at least 3 characters long and contain only alphabetic characters. The resulting list should be sorted in descending order based on the length of the names, maintaining the relative order of names with the same length.
"""

def name_lengths(names):
    """
    This function takes a list of names, filters out names with less than 3 characters or non-alphabetic characters,
    and returns a list of lengths of the remaining names in descending order.

    Args:
        names (list): A list of names

    Returns:
        list: A list of lengths of the names
    """
    return sorted([len(name) for name in names if len(name) >= 3 and name.isalpha()], reverse=True)