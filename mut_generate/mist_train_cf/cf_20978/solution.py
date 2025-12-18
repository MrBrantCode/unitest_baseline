"""
QUESTION:
Write a function `remove_duplicates` that takes a list as input, removes all duplicate elements from the list, and returns the result. The function must not use any built-in Python functions or libraries. The time complexity of the function should be O(n), where n is the length of the list. The list can contain any type of elements.
"""

def remove_duplicates(lst):
    result = []
    seen = set()

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result