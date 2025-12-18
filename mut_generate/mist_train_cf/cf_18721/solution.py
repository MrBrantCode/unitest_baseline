"""
QUESTION:
Write a function named `remove_second_to_last` that takes a list of integers as input, removes the second to last element if the list contains at least two elements, and returns the modified list.
"""

def remove_second_to_last(lst):
    if len(lst) >= 2:
        lst.pop(-2)
    return lst