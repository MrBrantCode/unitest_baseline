"""
QUESTION:
Create a function named `delete_occurrences` that takes two parameters: a list and an item to be deleted. The function should delete all occurrences of the specified item from the list without using any built-in list manipulation functions or methods and return the resulting list.
"""

def delete_occurrences(lst, item):
    result = []
    for element in lst:
        if element != item:
            result.append(element)
    return result