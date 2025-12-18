"""
QUESTION:
Write a function `find_max_in_nested_list` that takes a nested list of numerical values as input and returns the highest numerical value without using built-in sorting or max functions. The input list can have an arbitrary amount of nesting.
"""

def find_max_in_nested_list(nested_list):
    max_num = None
    
    for element in nested_list:
        if isinstance(element, list):
            num = find_max_in_nested_list(element)
        else:
            num = element
            
        if max_num is None or num > max_num:
            max_num = num
    
    return max_num