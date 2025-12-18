"""
QUESTION:
Implement a function named `remove_duplicates` that removes duplicate elements from a given list while preserving the original order. The function should achieve this in a time complexity of O(n), where n is the length of the list.
"""

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result