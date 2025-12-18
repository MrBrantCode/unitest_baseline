"""
QUESTION:
Implement a recursive function `is_sorted` that checks if a given list of integers is sorted in non-decreasing order. The function should return `True` if the list is sorted correctly and `False` otherwise. The time complexity of the solution should be O(n log n) and the space complexity should be O(log n). You can only use recursion, without any built-in sorting functions or loops.
"""

def is_sorted(lst):
    # Base cases
    if len(lst) <= 1:
        return True
    
    # Recursive case
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    return is_sorted(left) and is_sorted(right) and left[-1] <= right[0]