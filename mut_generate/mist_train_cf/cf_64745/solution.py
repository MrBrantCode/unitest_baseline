"""
QUESTION:
Create a function called `reverse_list` that takes a list of integers as input and returns the reversed list as a tuple. The function should not use the built-in `reverse()` function or list slicing.
"""

def entance(lst):
    new_lst = []
    for i in range(len(lst)-1, -1, -1):
        new_lst.append(lst[i])
    return tuple(new_lst)