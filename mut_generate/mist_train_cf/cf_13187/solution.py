"""
QUESTION:
Implement a function `find_min_recursive` that takes a list of numbers as input and returns the minimum value in the list without using any built-in functions or libraries. The function should use a recursive approach to find the minimum value.
"""

def find_min_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_rest = find_min_recursive(lst[1:])
        if lst[0] < min_rest:
            return lst[0]
        else:
            return min_rest