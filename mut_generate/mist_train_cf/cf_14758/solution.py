"""
QUESTION:
Write a function named `reverse_list` that takes a list as an argument and returns the reversed list without using the built-in `reverse()` method. The function should modify the input list in-place. The input list may contain any type of elements and may be empty.
"""

def entance(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst