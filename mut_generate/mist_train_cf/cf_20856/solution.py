"""
QUESTION:
Create a function called `find_common_elements` that takes two lists as input, `list1` and `list2`, and returns a set of common elements between the two lists. The function should not use any built-in functions or methods for finding intersections or common elements between lists. The time complexity of the function should be O(n), where n is the length of the longer list, and the space complexity should be O(1), where the size of the set is limited to the number of common elements.
"""

def find_common_elements(list1, list2):
    common_elements = set()
    for elem in list1:
        common_elements.add(elem)
    for elem in list2:
        if elem in common_elements:
            common_elements.add(elem)
    return common_elements