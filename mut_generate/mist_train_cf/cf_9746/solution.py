"""
QUESTION:
Create a function `remove_duplicates` that takes a list `lst` as input and returns a new list with all duplicate items removed, while preserving the original order of elements. The function must achieve a time complexity of O(n), where n is the size of the input list.
"""

def remove_duplicates(lst):
    seen = {}
    result = []
    for item in lst:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result