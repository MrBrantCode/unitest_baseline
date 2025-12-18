"""
QUESTION:
Create a function named `find_position` that takes a list and an item as parameters and returns the numerical position of the item in the list using zero-based indexing. If the item does not exist in the list, the function should return a message stating that the item does not exist in the list.
"""

def find_position(lst, item):
    if item in lst:
        return lst.index(item)
    else:
        return "Item does not exist in the list"