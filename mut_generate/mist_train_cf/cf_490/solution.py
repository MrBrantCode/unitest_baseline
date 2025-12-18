"""
QUESTION:
Write a function named `find_indices` that takes in two parameters: an array `arr` that may contain duplicate values and/or nested arrays as elements, and an item `x`. The function should return a list of tuples representing the indices of all occurrences of `x` in `arr`, including indices of `x` within nested arrays.
"""

def find_indices(arr, x):
    indices = []
    
    def search_nested_array(nested_arr, index):
        for i, val in enumerate(nested_arr):
            if val == x:
                indices.append(index + (i,))
            if isinstance(val, list):
                search_nested_array(val, index + (i,))
    
    for i, val in enumerate(arr):
        if val == x:
            indices.append((i,))
        if isinstance(val, list):
            search_nested_array(val, (i,))
    
    return indices