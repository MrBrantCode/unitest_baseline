"""
QUESTION:
Create a function called `remove_duplicates` that takes a list as input and returns a new list with duplicate elements removed while maintaining the original order of the elements. The function should have a time complexity of O(n).
"""

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result