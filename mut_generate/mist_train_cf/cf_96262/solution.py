"""
QUESTION:
Write a function `search_element(lst, element, index=0)` that searches for a given `element` in a list `lst` and returns the index of the first occurrence of the element. If the element is not found, the function should return -1. The function should use a single recursive call for the search algorithm. The list `lst` contains unique elements.
"""

def entance(lst, element, index=0):
    if index == len(lst):
        return -1
    if lst[index] == element:
        return index
    return entance(lst, element, index+1)