"""
QUESTION:
Write a function called `find_indices` that takes in an array `arr` and an item `x` as parameters. The function should return a list of tuples, where each tuple contains the indices of all occurrences of `x` in `arr`. If `x` is found within a nested array, the tuple should contain the index of the nested array and the index of `x` within the nested array. The function should handle arrays that may contain duplicate values and nested arrays as elements.
"""

def find_indices(arr, x):
    indices = []
    
    def search_nested_array(nested_arr, index):
        for i, val in enumerate(nested_arr):
            if val == x:
                indices.append((index, i))
            if isinstance(val, list):
                search_nested_array(val, index)
    
    for i, val in enumerate(arr):
        if val == x:
            indices.append((i,))
        if isinstance(val, list):
            search_nested_array(val, i)
    
    return indices