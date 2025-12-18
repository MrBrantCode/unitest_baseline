"""
QUESTION:
Create a function `select_names` that takes a list of names as input and returns a new list containing the names that start with 'A' and have a length greater than 5. The resulting list should be sorted in descending order based on the length of the names.
"""

def select_names(names):
    """
    Returns a new list containing the names that start with 'A' and have a length greater than 5.
    The resulting list is sorted in descending order based on the length of the names.

    Args:
        names (list): A list of names.

    Returns:
        list: A list of names that meet the specified criteria.
    """
    return sorted([name for name in names if name.startswith('A') and len(name) > 5], key=lambda x: len(x), reverse=True)