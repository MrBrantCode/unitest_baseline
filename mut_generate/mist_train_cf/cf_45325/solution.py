"""
QUESTION:
Create a function `sort_remove_duplicates` that takes a list of numerical values as input, replaces null or None values with zero, removes duplicates, and returns a sorted list. The function should handle missing values and prioritize high efficiency. The input list may contain any combination of integers, floats, and null or None values.
"""

def sort_remove_duplicates(lst):
    """Sort the list, replace None values with zeros and remove duplicates"""
    lst = [0 if i is None else i for i in lst] # replace None with zero 
    return sorted(list(set(lst))) # remove duplicates and sort