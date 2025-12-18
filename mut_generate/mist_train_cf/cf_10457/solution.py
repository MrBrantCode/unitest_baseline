"""
QUESTION:
Write a function named `find_common_items` that takes two lists as input and returns a list containing all unique common items between the two lists. The input lists can contain integers (positive and negative), floating-point numbers, and strings, with a maximum length of 1000.
"""

def find_common_items(list1, list2):
    common_items = set()
    
    for item in list1:
        if item in list2:
            common_items.add(item)
    
    return list(common_items)