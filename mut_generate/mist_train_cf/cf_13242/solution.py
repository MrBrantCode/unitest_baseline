"""
QUESTION:
Write a recursive function `find_max` that takes a list of integers as input and returns the maximum element in the list. If the list is empty, return `None`. Do not use any built-in functions like `max()` or `sort()`. The function should recursively divide the list into two halves until it reaches a list with one or zero elements, then compare and return the maximum element.
"""

def find_max(lst):
    # Base case: if the list is empty, return None
    if len(lst) == 0:
        return None

    # Base case: if the list contains only one element, return that element
    if len(lst) == 1:
        return lst[0]

    # Divide the list into two halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Recursively find the maximum element in each half
    max_left = find_max(left_half)
    max_right = find_max(right_half)

    # Compare the maximum elements of the two halves and return the larger one
    return max_left if max_left > max_right else max_right