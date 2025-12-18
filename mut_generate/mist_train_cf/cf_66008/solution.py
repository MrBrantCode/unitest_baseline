"""
QUESTION:
Write a function `next_smallest` that takes a list of integers as input and returns the second smallest element in the list. If the list has less than two distinct elements, return `None`. The function should be able to handle empty lists and lists with duplicate elements.
"""

def next_smallest(lst):
    if len(lst) < 2:
        return None
    sorted_lst = sorted(set(lst))
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]