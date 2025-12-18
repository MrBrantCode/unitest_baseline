"""
QUESTION:
Write a function named `reverse_list` that takes a list as input and returns the reversed list using recursion, without utilizing the built-in `reverse()` function. The function should work with lists of any length, including empty lists.
"""

def reverse_list(lst):
    if len(lst) <= 1:  # Base case: if the list is empty or has only one element
        return lst
    else:
        return reverse_list(lst[1:]) + [lst[0]]