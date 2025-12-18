"""
QUESTION:
Develop a function `remove_element_at_index` that takes a list `lst` and an integer `index` as inputs, and returns the list with the element at the specified `index` removed, while maintaining the order of the remaining elements. The function should have a time complexity of O(n), where n is the length of the list. If the `index` is out of range, return the original list.
"""

def remove_element_at_index(lst, index):
    if index < 0 or index >= len(lst):
        return lst
    else:
        return lst[:index] + lst[index+1:]