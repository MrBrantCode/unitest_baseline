"""
QUESTION:
Implement a function `compare_lists(list1, list2, func=None)` that compares two lists of numbers and returns a new list with the elements that are common to both lists. The function should be able to take an optional third argument `func`, which is a function itself, used to transform the elements before comparison. If `func` is not provided, the comparison should be done directly on the original elements. The function should be implemented in a functional programming style, avoiding the use of explicit loops.
"""

def compare_lists(list1, list2, func=None):
    if func is not None:
        list1 = list(map(func, list1))
        list2 = list(map(func, list2))
    
    # The logic to identify common elements using list comprehension
    return [item for item in list1 if item in list2]