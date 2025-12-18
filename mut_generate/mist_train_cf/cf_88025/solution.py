"""
QUESTION:
Write a function `find_max_value(d)` that takes a dictionary `d` as input, where `d` can be a nested dictionary with multiple levels of nesting, and its values can be either a single value or a list of values. The function should return the maximum value among all the values in the dictionary, considering all levels of nesting.
"""

def entrance(d):
    max_value = float('-inf')  # initialize max_value with negative infinity
    
    for value in d.values():
        if isinstance(value, dict):  # if the value is a dictionary, recursively call the function
            max_value = max(max_value, entrance(value))
        elif isinstance(value, list):  # if the value is a list, find the maximum score in the list
            max_value = max(max_value, max(value))
        else:  # if the value is a single value, update max_value if necessary
            max_value = max(max_value, value)
    
    return max_value