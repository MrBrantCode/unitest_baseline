"""
QUESTION:
Create a function `remove_all_occurrences(lst, item)` that takes a list `lst` and an item `item` as input, and returns a new list with all occurrences of `item` removed from `lst`. The function should not modify the original list.
"""

def remove_all_occurrences(lst, item):
    lst = [x for x in lst if x != item]
    return lst