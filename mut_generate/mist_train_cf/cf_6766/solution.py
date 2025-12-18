"""
QUESTION:
Write a function named `find_differences` that takes two lists, `list_a` and `list_b`, as input and returns a new list containing unique elements present in `list_a` but not in `list_b` and vice versa, considering both values and order of elements. The function should not use built-in functions or libraries for set operations or list manipulations, have a time complexity of O(n) or better, and handle large input lists efficiently without using additional data structures or auxiliary lists.
"""

def find_differences(list_a, list_b):
    differences = []
    for element in list_a:
        if element not in list_b:
            differences.append(element)
    for element in list_b:
        if element not in list_a:
            differences.append(element)
    return list(dict.fromkeys(differences))