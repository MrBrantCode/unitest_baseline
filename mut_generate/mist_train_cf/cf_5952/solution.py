"""
QUESTION:
Design a function named `remove_duplicates` that takes a list as input and returns a new list with duplicate elements removed, while preserving the original order. The function should consider elements with the same value but different case as duplicates, and remove any elements that have a duplicate elsewhere in the list, regardless of their position or case.
"""

def remove_duplicates(lst):
    unique = []
    seen = set()
    for item in lst:
        lower_item = item.lower()
        if lower_item not in seen:
            unique.append(item)
            seen.add(lower_item)
    return unique