"""
QUESTION:
Create a function `find_unique_elements` that takes two lists `list1` and `list2` as input and returns a new list consisting of elements which are present in only one of the lists. The function should not use any built-in Python functions or methods such as `set()` or list comprehension. The time complexity should be O(n^2), where n is the length of the longer list, and it should use only a single loop or equivalent structure with no nested loops or recursion.
"""

def find_unique_elements(list1, list2):
    unique_elements = []
    for element in list1:
        if element not in list2:
            unique_elements.append(element)
    for element in list2:
        if element not in list1:
            unique_elements.append(element)
    return unique_elements