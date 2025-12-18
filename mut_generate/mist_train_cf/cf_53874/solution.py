"""
QUESTION:
Write a function called `swap_values` that takes a multi-dimensional list and two values as input, and returns the list with all occurrences of the two values swapped. The function should handle lists of variable lengths and dimensions, whether known or unknown.
"""

def swap_values(lst, val1, val2):
    """ Swap all occurrences of val1 and val2 in the multi-dimensional list lst. """
    return [
        swap_values(i, val1, val2) if isinstance(i, list) 
        else val2 if i == val1 
        else val1 if i == val2 
        else i 
        for i in lst
    ]