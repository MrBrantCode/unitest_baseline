"""
QUESTION:
Write a function named `remove_duplicates` that takes a list `lst` as input, removes duplicate elements while preserving the original order, and returns the resulting list. The function should achieve a time complexity of O(n), where n is the length of the list, without using any built-in functions.
"""

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result