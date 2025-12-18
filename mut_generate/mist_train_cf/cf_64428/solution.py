"""
QUESTION:
Design a function named `second_smallest` that takes four arrays of integers as input, each containing at least four elements. The function should return the second smallest value from each array. The solution should have optimal space complexity.
"""

def second_smallest(arr1, arr2, arr3, arr4):
    return [sorted(arr)[1] for arr in [arr1, arr2, arr3, arr4]]