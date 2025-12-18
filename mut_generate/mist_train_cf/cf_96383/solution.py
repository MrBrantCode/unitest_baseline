"""
QUESTION:
Write a function `remove_duplicates(lst)` that takes a list `lst` as input and returns a new list containing all unique elements from `lst`. The function should not use any built-in Python functions or libraries. The time complexity of the function should be O(n), where n is the length of the list `lst`. The list `lst` can contain any type of elements.
"""

def remove_duplicates(lst):
    result = []
    seen = set()

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result