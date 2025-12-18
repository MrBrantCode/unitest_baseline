"""
QUESTION:
Write a function `getRangeAndModify(lst, min, max)` that takes a list of numbers and a range defined by `min` and `max` as input. The function should return a list of numbers within the given range, where even numbers are increased by 50% and odd numbers are reduced by 25%, sorted in ascending order. The function should have a time complexity of O(n log n) or less.
"""

def getRangeAndModify(lst, min_val, max_val):
    return sorted([item * 1.5 if item % 2 == 0 else item * 0.75 for item in lst if min_val <= item <= max_val])