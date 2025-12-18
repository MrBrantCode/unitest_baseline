"""
QUESTION:
Write a function named `find_common_elements` that takes two lists, `list1` and `list2`, as input and returns a list of elements that are present in both lists. The function should not use any built-in Python functions or libraries, except for basic operations like looping and conditional statements. The function should efficiently handle large lists, ideally with a time complexity better than O(n^2).
"""

def find_common_elements(list1, list2):
    common_elements = []
    set1 = set(list1)

    for element in list2:
        if element in set1:
            common_elements.append(element)

    return common_elements