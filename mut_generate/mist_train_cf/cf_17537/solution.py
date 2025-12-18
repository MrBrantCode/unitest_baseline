"""
QUESTION:
Write a function `reverse_list(lst)` that takes a list as input and returns the reversed list. The function must not use any built-in list functions, additional memory space, or any looping constructs. It should rely solely on recursive operations.
"""

def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    else:
        return reverse_list(lst[1:]) + [lst[0]]