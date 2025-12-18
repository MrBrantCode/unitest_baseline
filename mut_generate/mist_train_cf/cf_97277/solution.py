"""
QUESTION:
Write a function called `reverse_list` that takes a list as an argument and reverses the order of its elements in-place using recursion and basic operations such as indexing and swapping, without using any built-in or library functions for list manipulation.
"""

def entance(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1

    if start >= end:
        return lst

    lst[start], lst[end] = lst[end], lst[start]

    return entance(lst, start + 1, end - 1)