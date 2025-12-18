"""
QUESTION:
Implement a function `get_list_length(lst)` that takes a list `lst` as input and returns the number of elements in the list without using the built-in `len()` function or the `len()` method of the list object.
"""

def get_list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count