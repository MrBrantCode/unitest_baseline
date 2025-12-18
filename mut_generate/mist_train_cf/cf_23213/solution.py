"""
QUESTION:
Write a function `find_length(lst)` that calculates the total count of elements in a given list, including elements in nested lists, without using any built-in functions or methods. The function should recursively handle nested lists and return the total count.
"""

def find_length(lst):
    count = 0

    for item in lst:
        if isinstance(item, list):
            count += find_length(item)
        else:
            count += 1

    return count