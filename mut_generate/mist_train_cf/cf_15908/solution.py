"""
QUESTION:
Write a function `find_max_value` that finds the maximum value from a nested dictionary where the nested dictionary can have any number of levels and each level can have any number of keys and values, and the values can be either integers or lists of integers. The function should have a time complexity of O(n), where n is the total number of values in the nested dictionary.
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