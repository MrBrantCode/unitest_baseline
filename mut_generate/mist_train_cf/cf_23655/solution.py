"""
QUESTION:
Write a function `remove_duplicates` that takes a list of values as input and returns a new list with duplicate items removed, preserving the original order of elements.
"""

def remove_duplicates(list_values):
    result = []
    for i in list_values:
        if i not in result:
            result.append(i)
    return result