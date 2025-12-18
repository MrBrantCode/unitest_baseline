"""
QUESTION:
Write a function named `switch_first_last` that takes a list of elements as input and returns the list with the first and last elements swapped. The function should modify the original list.
"""

def switch_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst