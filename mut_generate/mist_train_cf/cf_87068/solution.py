"""
QUESTION:
Write a function named `add_item_to_list` that takes in a list `lst` and an item, and returns the index position of the item in the list. If the item is added to the list, return its new index position. If the item is already in the list, return the index position of the existing item. If the list is empty, return -1. The function should also print an error message if the list is empty, and a warning message if the item is already in the list.
"""

def add_item_to_list(lst, item):
    if len(lst) == 0:
        print("Error: List is empty")
        return -1
    elif item in lst:
        print("Warning: Item already in list")
        return lst.index(item)
    else:
        lst.append(item)
        return lst.index(item)