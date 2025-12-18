"""
QUESTION:
Create a function `flatten_list` that takes a nested list as input and returns the list in a flattened format. The function should be able to handle nested lists up to any level deep and should not use any built-in or external libraries to flatten the list. The input list can contain elements of any data type, including strings, floats, and integers.

Additionally, create a function `count_integers` that takes the flattened list as input and returns the count of integers in the list.
"""

def flatten_list(nested_list, flattened_list=None):
    """Flattens a nested list into a single list."""
    if flattened_list is None:
        flattened_list = []
    
    for element in nested_list:
        if isinstance(element, list):
            flatten_list(element, flattened_list)
        else:
            flattened_list.append(element)
    
    return flattened_list

def count_integers(flattened_list):
    """Counts the number of integers in a list."""
    count = 0
    for element in flattened_list:
        if isinstance(element, int):
            count += 1
    return count