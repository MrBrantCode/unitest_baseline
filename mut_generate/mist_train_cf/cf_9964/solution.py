"""
QUESTION:
Create a function named `get_unique_items` that takes a list of integers, floats, and/or strings as input and returns a new list containing only the items that appear once in the original list.
"""

def get_unique_items(lst):
    unique_items = []
    for item in lst:
        if lst.count(item) == 1:
            unique_items.append(item)
    return unique_items