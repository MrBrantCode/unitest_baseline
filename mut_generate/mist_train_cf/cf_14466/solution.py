"""
QUESTION:
Write a function named `find_common_elements` that takes two lists `list1` and `list2` as arguments and returns a list of elements that are common to both `list1` and `list2`, preserving the order of elements as they appear in `list1`. The function should be able to handle elements of different data types.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements