"""
QUESTION:
Write a function `common_elements(list1, list2)` that takes two lists of elements of different data types as input, and returns a list of elements that are common to both lists. The function should ignore any duplicates within each list, consider them as one occurrence, and return the common elements in the same order as they appear in the first list.
"""

def common_elements(list1, list2):
    set1 = set(list1)  # convert list1 to a set to remove duplicates
    common = [element for element in list2 if element in set1]
    return common