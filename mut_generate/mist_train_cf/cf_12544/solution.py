"""
QUESTION:
Create a function named `flatten_list` that takes a two-dimensional list as input and returns a one-dimensional list with all duplicate elements removed. The function should not use any built-in list flattening or set functions, but instead use nested loops to iterate over the input list.
"""

def flatten_list(lst):
    flattened_list = []
    for sublist in lst:
        for element in sublist:
            if element not in flattened_list:
                flattened_list.append(element)
    return flattened_list