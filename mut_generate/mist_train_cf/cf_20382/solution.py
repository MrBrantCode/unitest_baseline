"""
QUESTION:
Write a function called `find_intersecting_elements` that takes two lists of any data type as input and returns a list of their intersecting elements. The function should have a time complexity of O(n) and should not use any built-in functions or libraries.
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