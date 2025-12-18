"""
QUESTION:
Write a function named `reverse_list` that takes a list as input and returns the reversed list. The function must use recursion and cannot use any loops or the built-in `reverse()` function. The input list can be empty, contain duplicate elements, nested lists, and different data types.
"""

def reverse_list(lst):
    # Base Case
    if len(lst) <= 1:
        return lst

    # Recursive Case
    return reverse_list(lst[1:]) + [lst[0]]