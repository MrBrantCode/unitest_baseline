"""
QUESTION:
Write a function `find_common_elements` that takes two lists of integers as input and returns a set containing the common elements between the two lists. The function should have a time complexity of O(n), where n is the length of the longer list, and must use a single loop to iterate over the elements of the lists.
"""

def find_common_elements(list1, list2):
    common_elements = set()
    for element in list1:
        if element in list2:
            common_elements.add(element)
    return common_elements