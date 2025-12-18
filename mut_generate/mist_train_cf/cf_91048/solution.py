"""
QUESTION:
Develop a function `remove_duplicates` that takes a list as input, removes duplicate items while preserving the original order of elements, and returns the new list. The time complexity of the function should be O(n), where n is the size of the input list.
"""

def remove_duplicates(lst):
    seen = {}
    result = []
    for item in lst:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result