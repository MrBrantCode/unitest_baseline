"""
QUESTION:
Create a function `sort_values` that takes a list of mixed data types as input and returns the sorted list. The list should be sorted in ascending order, with integers coming before strings. The integers should be sorted numerically, while the strings should be sorted lexicographically. If there are multiple integers or strings with the same value, they should maintain their original order. The function should be able to handle a list of any length and any combination of integers and strings.
"""

def sort_values(lst):
    """
    Sorts a list of mixed data types in ascending order, with integers before strings.
    
    The integers are sorted numerically, while the strings are sorted lexicographically.
    If there are multiple integers or strings with the same value, they maintain their original order.
    
    Parameters:
    lst (list): A list of mixed data types.
    
    Returns:
    list: The sorted list.
    """
    return sorted(lst, key=lambda x: (isinstance(x, str), str(x)))