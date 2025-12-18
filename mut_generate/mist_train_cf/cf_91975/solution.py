"""
QUESTION:
Implement a function called `remove_all_duplicates` that takes in a list `lst` and an `element` as input. Remove all occurrences of the given `element` from the `list` and also eliminate any duplicates of that element if it already exists in the list. Return the modified list.
"""

def remove_all_duplicates(lst, element):
    """Remove all occurrences of the given element from the list and eliminate any duplicates of that element."""
    return [x for x in lst if x != element or lst.count(x) == 1]