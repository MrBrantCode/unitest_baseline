"""
QUESTION:
Write a function named `common_elements` that takes two lists as arguments and returns a list of unique elements that are common to both lists, preserving the order of elements as they appear in the first list, and handling elements of different data types.
"""

def common_elements(list1, list2):
    set1 = set(list1)  
    common = []
    for element in list1:
        if element in set1 and element in list2 and element not in common:
            common.append(element)
    return common