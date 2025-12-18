"""
QUESTION:
Create a function `delete_occurrences` that takes a list and an item as input and returns a new list with all occurrences of the specified item removed. The function should not use any built-in list manipulation functions or methods.
"""

def delete_occurrences(lst, item):
    result = []
    for element in lst:
        if element != item:
            result.append(element)
    return result