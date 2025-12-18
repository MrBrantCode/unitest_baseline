"""
QUESTION:
Write a function `last_occurrence` that takes a list of integers `lst` and a specific integer `value` as input. The function should return the index of the last occurrence of `value` in `lst`. If `value` is not found in `lst`, return -1. Do not use any built-in Python functions or libraries.
"""

def last_occurrence(lst, value):
    index = -1
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == value:
            index = i
            break
    return index