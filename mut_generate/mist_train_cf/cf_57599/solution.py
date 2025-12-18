"""
QUESTION:
Write a function `all_unique` that takes a list of strings as input and returns `True` if all strings in the list are unique and `False` otherwise.
"""

def all_unique(lst):
    return len(lst) == len(set(lst))