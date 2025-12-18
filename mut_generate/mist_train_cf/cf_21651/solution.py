"""
QUESTION:
Write a function `remove_item` that takes a list and an item as input, and returns the list with the first occurrence of the item removed. The function must have a time complexity of O(n) or better and cannot use any additional libraries or functions, including the built-in remove() function.
"""

def remove_item(lst, item):
    return [x for x in lst if x != item]