"""
QUESTION:
Create a function `double_values` that takes a multidimensional list of numbers as input. The function should modify the list in-place, doubling all numerical values, and return the modified list. The function should work recursively to handle nested lists of arbitrary depth.
"""

def double_values(lst):
    for i in range(len(lst)):
        if type(lst[i]) is list:
            double_values(lst[i])
        else:
            lst[i] *= 2
    return lst