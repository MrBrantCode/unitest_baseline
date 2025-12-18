"""
QUESTION:
Implement a function `is_sorted` that checks if a given list of integers is sorted in non-decreasing order. The function should return `True` if the list is sorted and `False` otherwise.
"""

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True