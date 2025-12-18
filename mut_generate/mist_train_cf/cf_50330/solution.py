"""
QUESTION:
Write a function `calcSize(lst)` that calculates the total number of elements in a nested list `lst`. The list can be nested to any depth, may not be symmetrically nested, and contains only integers. Do not use the built-in `len()` function.
"""

def calcSize(lst):
    count = 0
    for element in lst:
        if isinstance(element, list):
            count += calcSize(element)
        else:
            count += 1
    return count