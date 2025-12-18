"""
QUESTION:
Write a function `remove_element(lst, element)` to remove all occurrences of a specified `element` from a given list `lst` and return the modified list. The function must modify the original list in-place, have a time complexity of O(n), and not use built-in list methods such as `remove()`.
"""

def remove_element(lst, element):
    if len(lst) == 0:  # Empty List
        return lst

    index = 0
    while index < len(lst):
        if lst[index] == element:
            lst.pop(index)
        else:
            index += 1

    return lst