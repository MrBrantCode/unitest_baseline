"""
QUESTION:
Write a function `find_values` that finds the highest and lowest values within a list of integers. The function should return a tuple containing the lowest and highest values in that order. The function should also include error checking to handle an empty list, in which case it should return `None`.
"""

def find_values(lst):
    if not lst:  
        return None
    max_val = lst[0]
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    return min_val, max_val