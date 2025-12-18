"""
QUESTION:
Create a function called `flatten_list` that takes a 2D list of integers as input and returns a new 1D list containing all the elements from the input list. The function should not use the `copy.deepcopy()` function, any other built-in functions or libraries, temporary variables, or lists. The output list should be created by appending elements to an initially empty list.
"""

def flatten_list(nested_list):
    """Return a new 1D list containing all elements from the input 2D list."""
    result = []
    for sublist in nested_list:
        for element in sublist:
            result.append(element)
    return result