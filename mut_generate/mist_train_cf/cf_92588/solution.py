"""
QUESTION:
Design a function called `remove_duplicates` that takes a list as input, removes the duplicate elements while preserving the order of the elements, and also removes any elements that have a duplicate elsewhere in the list. The function should return a new list with the unique elements.
"""

def remove_duplicates(lst):
    seen = set()
    result = []
    duplicates = set()
    for element in lst:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    for element in lst:
        if element not in duplicates:
            if element not in result:
                result.append(element)
    return result