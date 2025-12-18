"""
QUESTION:
Implement a function named `find_common_elements` that takes two lists `lst1` and `lst2` as input and returns a new list containing their common elements. The function should have a time complexity of O(n), where n is the length of the longest input list, and should not use any built-in Python functions or libraries.
"""

def find_common_elements(lst1, lst2):
    # Create an empty set to store unique elements from lst1
    unique_elements = set()
    
    # Iterate through lst1 and add each element to the set
    for elem in lst1:
        unique_elements.add(elem)
    
    # Create an empty list to store common elements
    common_elements = []
    
    # Iterate through lst2 and check if each element is in the set
    for elem in lst2:
        if elem in unique_elements:
            common_elements.append(elem)
    
    return common_elements