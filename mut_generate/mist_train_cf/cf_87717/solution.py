"""
QUESTION:
Create a function named `find_common_elements` that takes two lists of integers as parameters. The function should return a new list containing the integers that are common in both input lists. The function must have a time complexity of O(n), where n is the length of the longer list, and handle cases where one or both input lists are empty by returning an empty list. The resulting list may contain duplicates and the order of elements does not matter.
"""

def find_common_elements(list1, list2):
    if not list1 or not list2:
        return []

    set1 = set(list1)
    set2 = set(list2)
    
    common_elements = set1.intersection(set2)
    
    return list(common_elements)