"""
QUESTION:
Construct a function named `process_lists` that takes two lists, `list_one` and `list_two`, as input and returns a new list. The new list should contain elements that are the result of a mathematical operation applied to corresponding items from `list_one` and `list_two`. The operation is to multiply each item from `list_one` by two and subtract the result from the corresponding item in `list_two`. The input lists are guaranteed to have the same length, and the order of items in the output list should match the order in the original lists.
"""

def process_lists(list_one, list_two):
    """Return a new list containing elements resulting from 
    multiplying items from list_one by two and subtracting 
    the result from corresponding items in list_two."""
    
    return [list_two[i] - (2 * list_one[i]) for i in range(len(list_one))]