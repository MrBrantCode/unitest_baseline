"""
QUESTION:
Implement a function named `is_sorted` that checks if a given list of integers is sorted in ascending order. The function should return `True` if the list is sorted in ascending order and `False` otherwise. The function must achieve a time complexity of O(n), where n is the length of the list.
"""

def entrance(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True