"""
QUESTION:
Write a function `is_sorted` that checks if a given list of integers is sorted in ascending order. The function should return `True` if the list is sorted and `False` otherwise. Assume the input list contains at least one element.
"""

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))