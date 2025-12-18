"""
QUESTION:
Implement a function `quicksort(lst)` that sorts a list of integers in ascending order, preserving the relative order of equal elements. The function should not use any built-in sorting functions. The input list can contain any integer values. The output should be a new sorted list.
"""

def quicksort(lst):
    """Quicksort over a list-like sequence."""
    if len(lst) == 0:
        return []

    pivot = lst[0]
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for x in lst:
        if x < pivot:
            less_than_pivot.append(x)
        elif x == pivot:
            equal_to_pivot.append(x)
        else:
            greater_than_pivot.append(x)
    
    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)