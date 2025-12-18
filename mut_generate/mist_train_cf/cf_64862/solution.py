"""
QUESTION:
Implement a function called `quick_sort` that takes a list of integers as input and returns the list sorted in ascending order. The function should use the quick sort algorithm, a 'divide and conquer' approach that partitions the input list around a pivot element and recursively sorts the sub-lists.
"""

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)