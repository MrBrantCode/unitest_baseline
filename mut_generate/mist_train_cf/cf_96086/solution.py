"""
QUESTION:
Write a function `find_intersecting_elements(list1, list2)` that determines the intersecting elements of two lists `list1` and `list2` without using any built-in functions or libraries. The function should have a time complexity of O(n) and be able to handle lists of any data type.
"""

def find_intersecting_elements(list1, list2):
    intersecting_elements = []
    list1_dict = {}
    
    # Create a dictionary to store elements of list1 as keys
    for element in list1:
        list1_dict[element] = True
    
    # Check if each element in list2 exists in the dictionary
    for element in list2:
        if element in list1_dict:
            intersecting_elements.append(element)
    
    return intersecting_elements