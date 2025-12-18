"""
QUESTION:
Write a function `filter_names` that filters a list of names to include only those longer than 5 characters and starting with "J", then returns them in alphabetical order.
"""

def filter_names(names):
    """
    Filters a list of names to include only those longer than 5 characters and starting with "J", 
    then returns them in alphabetical order.
    
    Parameters:
    names (list): A list of names.
    
    Returns:
    list: A list of filtered names.
    """
    return sorted([name for name in names if len(name) > 5 and name.startswith("J")])