"""
QUESTION:
Write a function `find_max_indices` that takes a list of integers as input and returns a list of the indices of the first, second, and third maximum values in the list. If there are duplicate maximum values, consider each instance of the maximum value at different indices as distinct.
"""

def find_max_indices(input_list):
    max_values = sorted(set(input_list), reverse=True)[:3]
    max_indices = {max_value: [] for max_value in max_values}
    
    for index, value in enumerate(input_list):
        if value in max_values:
            max_indices[value].append(index)
    
    all_indices = [index for indices in max_indices.values() for index in indices]
    
    return sorted(all_indices)[:3]