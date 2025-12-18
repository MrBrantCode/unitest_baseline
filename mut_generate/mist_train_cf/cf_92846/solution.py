"""
QUESTION:
Write a function `find_index(lst, element, index=0)` that finds the index of the first occurrence of `element` in list `lst`. The function should consider that `lst` may contain duplicate elements and `element` itself may be a list. The function should return the index of the first occurrence of `element`, or -1 if `element` is not found in `lst`.
"""

def find_index(lst, element, index=0):
    if index == len(lst):
        return -1

    if lst[index] == element:
        return index

    if isinstance(lst[index], list):
        sublist_index = find_index(lst[index], element)
        if sublist_index != -1:
            return index

    return find_index(lst, element, index + 1)