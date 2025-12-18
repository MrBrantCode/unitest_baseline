"""
QUESTION:
Implement a function named `find_common_elements` that takes two lists as input, `list1` and `list2`, and returns a list of elements present in both `list1` and `list2` without using any built-in Python functions or libraries. The function should be efficient for large lists.
"""

def find_common_elements(list1, list2):
    common_elements = []
    set1 = set(list1)

    for element in list2:
        if element in set1:
            common_elements.append(element)

    return common_elements