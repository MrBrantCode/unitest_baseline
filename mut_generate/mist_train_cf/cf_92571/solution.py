"""
QUESTION:
Create a function named `remove_duplicates` that takes a list as an input and returns a new list with duplicate elements removed. The function should not use built-in methods to remove duplicates and should maintain the original order of elements. The function should only use a single loop and should not modify the original list.
"""

def remove_duplicates(lst):
    result = []
    seen = set()

    for element in lst:
        if element not in seen:
            result.append(element)
            seen.add(element)

    return result