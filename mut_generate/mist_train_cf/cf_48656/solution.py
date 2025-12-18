"""
QUESTION:
Write a function `switch_positions` that takes a list of integers as input. If the list contains at least 5 elements, includes both negative and positive integers, and has no duplicates, switch the positions of the first and last elements and return the modified list. Otherwise, return 'Invalid list'.
"""

def switch_positions(lst):
    if len(lst) >= 5 and len(lst) == len(set(lst)) and any(i < 0 for i in lst) and any(i > 0 for i in lst):
        lst[0], lst[-1] = lst[-1], lst[0]
        return lst
    else:
        return 'Invalid list'