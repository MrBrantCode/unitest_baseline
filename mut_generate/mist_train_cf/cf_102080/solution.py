"""
QUESTION:
Write a function named `find_common_elements` that takes two lists, `list1` and `list2`, as input and returns a new list containing the unique common elements from both lists. The function should have a time complexity of O(n), where n is the total number of elements in the input lists, and should be able to handle large input lists efficiently. The function should also handle cases where the input lists may contain duplicates, and should only include unique common elements in the output list.
"""

def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)