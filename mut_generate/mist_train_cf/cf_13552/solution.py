"""
QUESTION:
Find the index of the first occurrence of a given element in a list. The list may contain duplicate elements and the element itself may be a list. Implement the solution using a recursive approach. The function should take three arguments: the list to search in, the element to find, and the current index being checked (defaulting to 0 if not provided). Return the index of the first occurrence of the element, or -1 if the element is not found.
"""

def entrance(lst, element, index=0):
    if index == len(lst):
        return -1

    if lst[index] == element:
        return index

    if isinstance(lst[index], list):
        sublist_index = entrance(lst[index], element)
        if sublist_index != -1:
            return index

    return entrance(lst, element, index + 1)