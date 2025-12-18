"""
QUESTION:
Implement a function `find_minimum(lst)` to find the minimum value in a list. The function should work for both numerical and non-numerical elements, handle lists with duplicate minimum values correctly, and not use any built-in functions or libraries. The function should also handle edge cases, such as an empty list.
"""

def find_minimum(lst):
    if len(lst) == 0:
        return None
    min_value = lst[0]
    for element in lst:
        if element < min_value:
            min_value = element
    return min_value