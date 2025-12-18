"""
QUESTION:
Create a function called `remove_duplicates` that takes a list as input and returns a new list containing the same elements in the same order but with duplicates removed. The function must only use a single loop and must not modify the original list.
"""

def entrance(lst):
    result = []
    seen = set()

    for element in lst:
        if element not in seen:
            result.append(element)
            seen.add(element)

    return result