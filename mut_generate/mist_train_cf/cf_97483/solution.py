"""
QUESTION:
Write a function named `find_length` that calculates the total number of elements in a given list, including those in nested lists, without using any built-in list methods or functions. The function should recursively traverse the list and its nested lists, counting each element, and return the total count.
"""

def find_length(lst):
    count = 0

    for item in lst:
        if isinstance(item, list):
            count += find_length(item)
        else:
            count += 1

    return count