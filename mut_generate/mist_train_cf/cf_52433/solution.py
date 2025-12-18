"""
QUESTION:
Develop a recursive function `find_min` that takes a list of lists of integers as input and returns the smallest numerical value present in the list. The function should discard non-integer values, including string representations of numbers, without causing an exception. If the list is empty or contains no integers, the function should return infinity.
"""

def find_min(lst, min_val=float('inf')):
    for i in lst:
        if isinstance(i, list):
            min_val = find_min(i, min_val)
        elif isinstance(i, int):
            if i < min_val:
                min_val = i
                
    return min_val