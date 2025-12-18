"""
QUESTION:
Create a function `replace_element` that replaces an element at a specific index in a list with a new element. The function should take a list, an index, and a new element as arguments, and return the updated list. Ensure the function checks if the index is within the range of the list to avoid an `IndexError`. The modification should occur in-place, updating the original list.
"""

def replace_element(lst, index, elem):
    if index < len(lst):
        lst[index] = elem
    return lst