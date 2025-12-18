"""
QUESTION:
Create a function `are_items_unique` that takes a list of items as an argument and returns `True` if all items in the list are unique and `False` otherwise, without using any built-in functions or data structures.
"""

def are_items_unique(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True