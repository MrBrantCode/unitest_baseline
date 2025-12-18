"""
QUESTION:
Write a function `swap_first_last` that takes a list of elements as input and swaps the first and last items if the list has more than one element.
"""

def swap_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst