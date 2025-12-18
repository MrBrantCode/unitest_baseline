"""
QUESTION:
Write a recursive function `reverse_list` that takes a list of elements as input and returns the same list with its elements in reverse order, without using any iterative methods or built-in reverse functions. The input list can be empty.
"""

def reverse_list(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_list(lst[:-1])