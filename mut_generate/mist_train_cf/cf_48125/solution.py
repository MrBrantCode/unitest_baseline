"""
QUESTION:
Write a recursive function `find_min(lst)` that finds the smallest integer in a list that may contain sub-lists. The function should handle nested lists of arbitrary depth and return the smallest integer found. The function should not use any additional Python libraries.
"""

def find_min(lst):
    # Base Case: if the list is empty
    if not lst:
        return float('inf')  # return a very large number
    
    # if first element is a list, find minimum in it
    if isinstance(lst[0], list):
        a = find_min(lst[0])
    else:
        a = lst[0]
        
    # find minimum in the rest of the list
    b = find_min(lst[1:])
    
    # return the smaller one
    return a if a < b else b