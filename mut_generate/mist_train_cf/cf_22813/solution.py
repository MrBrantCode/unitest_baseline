"""
QUESTION:
Write a function named `reverse_list` that takes a list and two optional parameters, `start` and `end`, and reverses the order of the elements in the list in-place using recursion. The function should not use any built-in or library functions for list manipulation, only basic operations such as indexing and swapping. If `end` is not provided, it should default to the last index of the list.
"""

def reverse_list(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1

    if start >= end:
        return lst

    lst[start], lst[end] = lst[end], lst[start]

    return reverse_list(lst, start + 1, end - 1)