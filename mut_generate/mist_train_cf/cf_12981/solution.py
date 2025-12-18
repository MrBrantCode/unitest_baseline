"""
QUESTION:
Design a function called `remove_duplicates` that takes a list as input and returns a new list with all duplicate elements removed, preserving the original order of unique elements. The function should also remove any elements that appear more than once in the input list, regardless of their position.
"""

def remove_duplicates(lst):
    seen = set()
    result = []
    for element in lst:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result