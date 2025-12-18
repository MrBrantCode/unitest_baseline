"""
QUESTION:
Write a function `manage_duplicates(lst)` that takes a list of strings as input, replaces any duplicate values with 'X', and maintains the original order of the list. The function should handle lists with zero, one, or multiple duplicates.
"""

def manage_duplicates(lst):
    seen = set()
    for i, val in enumerate(lst):
        if val in seen:
            lst[i] = "X"
        else:
            seen.add(val)
    return lst