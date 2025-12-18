"""
QUESTION:
Create a function `merge_sorted_arrays` that merges two sorted arrays `a` and `b` into a single sorted array. The function should take two parameters `a` and `b`, which are lists of integers that are already sorted in ascending order. The function should return a new list that contains all elements from `a` and `b` in sorted order.
"""

def merge_sorted_arrays(a, b):
    # concatenate both arrays
    c = a + b
    # sort resulting array
    c.sort()
    # return sorted array
    return c