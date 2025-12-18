"""
QUESTION:
Create a function `find_common_elements(list1, list2)` that takes two lists of integers as parameters. The function should return a list of integers that are common in both input lists. The function must have a time complexity of O(n), where n is the length of the longer list, and it must handle the case when one or both input lists are empty by returning an empty list. The order of elements in the resulting list does not matter, and the lists can contain duplicates.
"""

def find_common_elements(list1, list2):
    if not list1 or not list2:
        return []

    set1 = set(list1)
    set2 = set(list2)
    
    common_elements = set1.intersection(set2)
    
    return list(common_elements)