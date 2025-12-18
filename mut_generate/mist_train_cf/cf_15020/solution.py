"""
QUESTION:
Write a function called `reverse_list` that takes one parameter, a list of integers, and returns the list in reverse order. Do not use the built-in `reverse()` method or the `[::-1]` slicing syntax.
"""

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst