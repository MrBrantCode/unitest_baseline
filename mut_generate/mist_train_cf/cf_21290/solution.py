"""
QUESTION:
Create a function `filter_and_sort_names` that takes a list of names as input and returns a new list containing names that start with 'A' and have a length greater than 5. The resulting list should be sorted in descending order based on the length of the names. If multiple names have the same length, they should be sorted alphabetically in ascending order.
"""

def filter_and_sort_names(names):
    """
    This function filters names that start with 'A' and have a length greater than 5, 
    then sorts them in descending order based on the length of the names. 
    If multiple names have the same length, they are sorted alphabetically in ascending order.

    Args:
        names (list): A list of names

    Returns:
        list: A new list containing filtered and sorted names
    """
    return sorted([name for name in names if name.startswith('A') and len(name) > 5], key=lambda x: (-len(x), x))