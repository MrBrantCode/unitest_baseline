"""
QUESTION:
Create a function named `find_common_elements` that takes two lists, `list1` and `list2`, as parameters. The function should return a new list containing the elements that are common to both lists. The function should not use any built-in Python functions that find common elements between lists, such as `set.intersection()`.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements