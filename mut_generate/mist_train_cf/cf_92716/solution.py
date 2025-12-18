"""
QUESTION:
Implement a recursive function `find_max` that takes a list of integers as input and returns the maximum element in the list without using built-in functions like `max()` or `sort()`. The function should divide the input list into two halves, recursively find the maximum element in each half, and return the larger one. If the input list is empty, return `None`. If the list contains only one element, return that element.
"""

def find_max(lst):
    if len(lst) == 0:
        return None

    if len(lst) == 1:
        return lst[0]

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    max_left = find_max(left_half)
    max_right = find_max(right_half)

    return max_left if max_left > max_right else max_right