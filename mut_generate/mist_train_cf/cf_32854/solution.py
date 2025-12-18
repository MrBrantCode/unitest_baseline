"""
QUESTION:
Implement a function `search_name` that takes a list of names and a target name as input, and returns `True` if the target name is found in the list (case-insensitive) and `False` otherwise.
"""

def search_name(name_list, target_name):
    """
    Searches for a target name in a list of names (case-insensitive).
    
    Args:
        name_list (list): A list of names.
        target_name (str): The target name to search for.
    
    Returns:
        bool: True if the target name is found, False otherwise.
    """
    return target_name.casefold() in [name.casefold() for name in name_list]