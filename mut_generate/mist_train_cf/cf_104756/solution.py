"""
QUESTION:
Write a function `check_item(lst, item)` that takes a list `lst` and an item as input, and returns a tuple containing the index of the first occurrence of the item in the list and the total number of occurrences of the item. If the item is not found in the list, return -1 for the index and the count of occurrences.
"""

def check_item(lst, item):
    count = lst.count(item)
    if count == 0:
        return -1, count
    else:
        index = lst.index(item)
        return index, count