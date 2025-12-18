"""
QUESTION:
Create a function `find_max` that takes a list of integers as input and returns the maximum value in the list without using the built-in max() function. The function should be implemented using recursion and should handle lists that may contain negative numbers or be empty.
"""

def find_max(lst):
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    left_max = find_max(lst[:mid])
    right_max = find_max(lst[mid:])
    if left_max is None:
        return right_max
    elif right_max is None:
        return left_max
    else:
        return left_max if left_max > right_max else right_max