"""
QUESTION:
Implement a function `remove_duplicates` that removes duplicate elements from a given list while maintaining the original order of elements. The function should achieve this in a time complexity of O(n), where n is the length of the list, without using any built-in functions.
"""

def remove_duplicates(lst):
    unique_lst = []
    seen = set()

    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)

    return unique_lst