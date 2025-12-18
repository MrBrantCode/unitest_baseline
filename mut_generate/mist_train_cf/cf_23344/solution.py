"""
QUESTION:
Write a function `modify_list` that takes a list of integers as input, appends a new element to the list for each existing element by adding 6 to the existing element, and returns the modified list.
"""

def modify_list(lst):
    """Appends a new element to the list for each existing element by adding 6 to the existing element."""
    return [x for x in lst] + [x + 6 for x in lst]