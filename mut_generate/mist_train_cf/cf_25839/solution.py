"""
QUESTION:
Write a function `filter_names_longer_than_5` to filter out the names that are 5 characters or less from a given list of names. The function should return a new list containing only the names longer than 5 characters.
"""

def filter_names_longer_than_5(names):
    """
    Filter out the names that are 5 characters or less from a given list of names.
    
    Args:
        names (list): A list of names.
    
    Returns:
        list: A new list containing only the names longer than 5 characters.
    """
    return [name for name in names if len(name) > 5]