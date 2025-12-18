"""
QUESTION:
Write a function named `find_common_elements` that takes two lists `list1` and `list2` as input and returns a list containing the common elements between the two lists. The function should use list comprehension and should not use the 'if' statement or any built-in functions or methods.
"""

def find_common_elements(list1, list2):
    return [item1 for item1 in list1 for item2 in list2 if item1 == item2]