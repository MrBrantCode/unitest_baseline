"""
QUESTION:
Write a function `find_max_value` that finds the maximum value in a nested dictionary. The nested dictionary can have any number of levels and each level can have any number of keys and values. The values can be either integers or lists of integers. The function should return the maximum value, which can be either a single integer or a list of integers. The time complexity of the solution should be O(n), where n is the total number of values in the nested dictionary.
"""

def find_max_value(nested_dict):
    max_value = float('-inf')
    
    for value in nested_dict.values():
        if isinstance(value, int):
            max_value = max(max_value, value)
        elif isinstance(value, list):
            max_value = max(max_value, max(value))
        else:
            max_value = max(max_value, find_max_value(value))
    
    return max_value