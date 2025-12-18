"""
QUESTION:
Create a function called `find_indices` that takes two lists, `first_list` and `second_list`, as input and returns the indices of elements in `first_list` that are also present in `second_list`. If an element from `second_list` appears multiple times in `first_list`, the function should return the index of the first occurrence.
"""

def find_indices(first_list, second_list):
    indices = []
    for element in second_list:
        if element in first_list:
            indices.append(first_list.index(element))
    return indices