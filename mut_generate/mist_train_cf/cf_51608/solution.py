"""
QUESTION:
Write a function `complex_list_sum(lst)` that calculates the sum of all integers in a list `lst`, which may contain nested lists and non-integer values. The function should recursively traverse the list and its sublists, adding up only the integer values, while ignoring non-integer values.
"""

def complex_list_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += complex_list_sum(item)
        elif isinstance(item, int):
            total += item
    return total