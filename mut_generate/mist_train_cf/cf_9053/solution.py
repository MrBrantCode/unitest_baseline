"""
QUESTION:
Write a function called `get_list_length` that takes a list as input and returns the number of elements in the list without using the built-in `len()` function or the `len()` method of the list object.
"""

def get_list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count