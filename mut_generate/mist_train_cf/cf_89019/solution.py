"""
QUESTION:
Write a function `reverse_list(lst)` that takes a list as input and returns the reversed list. The function must use recursion and cannot use the built-in `reverse()` function or any loops. The input list can be empty, contain duplicate elements, contain nested lists, and contain different data types.
"""

def reverse_list(lst):
    # Base Case
    if len(lst) <= 1:
        return lst

    # Recursive Case
    return reverse_list(lst[1:]) + [lst[0]]