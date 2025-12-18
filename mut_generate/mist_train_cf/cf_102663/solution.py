"""
QUESTION:
Write a function `remove_occurrences(lst, item)` that removes all occurrences of a given item from a list `lst` and returns the resulting list, maintaining the relative order of the remaining items. The function should have a time complexity of O(n), where n is the length of the list `lst`.
"""

def remove_occurrences(lst, item):
    result = []
    for element in lst:
        if element != item:
            result.append(element)
    return result