"""
QUESTION:
Construct a function `list_intersection(l1: list, l2: list)` that takes two lists `l1` and `l2` as input and returns their intersection without using built-in set functions. The function should return the intersection elements in sorted order without duplication, support lists with negative numbers and mixed data types, and have a time complexity of O(n).
"""

def list_intersection(l1: list, l2: list) -> list:
    # Using dictionary to store elements in list1
    dict_list1 = {i: True for i in l1}
    # Checking elements of list2 in dictionary and storing common elements in another dictionary
    common_elements = {i: True for i in l2 if i in dict_list1}
    # Sorting and returning the keys which are the common elements
    return sorted(common_elements.keys())