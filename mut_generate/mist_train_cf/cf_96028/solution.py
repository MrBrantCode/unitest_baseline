"""
QUESTION:
Implement a function named `reverse_list` that takes a list as input and returns the reversed list. The function must use recursion and cannot use the built-in `reverse()` function. The function should be able to handle lists of any length, including empty lists and lists with one element.
"""

def reverse_list(lst):
    if len(lst) <= 1:  # Base case: if the list is empty or has only one element
        return lst
    else:
        return reverse_list(lst[1:]) + [lst[0]]