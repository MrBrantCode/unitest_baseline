"""
QUESTION:
Create a function named `filter_names` that takes a list of names as input, filters out names with four characters or less, and checks for duplicate names. The function should return a list of names with more than four characters and a boolean indicating whether there are any duplicate names in the input list.
"""

def filter_names(names):
    """
    Filters out names with four characters or less and checks for duplicate names.

    Args:
        names (list): A list of names.

    Returns:
        list: A list of names with more than four characters.
        bool: A boolean indicating whether there are any duplicate names.
    """
    long_names = [name for name in names if len(name) > 4]
    has_duplicates = len(names) != len(set(names))
    return long_names, has_duplicates