"""
QUESTION:
Create a function called `find_common_elements` that takes two lists as input and returns their common elements. The function should have a time complexity of O(n), where n is the length of the longer list. It should not use any built-in functions or methods for finding intersections or common elements between lists, but it is allowed to use a set data structure for efficient lookups.
"""

def find_common_elements(list1, list2):
    common_elements = []
    set1 = set(list1)
    for element in list2:
        if element in set1:
            common_elements.append(element)
    return common_elements