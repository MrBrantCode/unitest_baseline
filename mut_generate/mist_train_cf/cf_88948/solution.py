"""
QUESTION:
Implement a recursive function named `is_sorted` that checks if a given list of integers is sorted in non-decreasing order. The function should return `True` if the list is sorted correctly and `False` otherwise. It should handle edge cases such as an empty list and a list with duplicate elements correctly. 

The function should have a time complexity of O(n log n) and a space complexity of O(log n). No built-in sorting functions or loops are allowed in the implementation.
"""

def is_sorted(lst):
    if len(lst) <= 1:
        return True

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    return is_sorted(left) and is_sorted(right) and left[-1] <= right[0]