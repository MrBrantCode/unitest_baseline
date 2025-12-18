"""
QUESTION:
Sort the given list of names in descending alphabetical order, excluding names that start with the letter 'A'. Implement a function called `sort_names` that takes a list of names as input and returns the sorted list.
"""

def sort_names(names):
    return sorted([name for name in names if not name.startswith('A')], reverse=True)