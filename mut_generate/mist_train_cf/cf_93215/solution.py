"""
QUESTION:
Write a function `find_common_elements(list1, list2)` that takes two lists as parameters and returns a third list containing the elements that occur in both lists. The function should have a time complexity of O(n), where n is the length of the longer list, and should not use built-in Python functions like intersection or set operations.
"""

def find_common_elements(list1, list2):
    common_elements = []
    
    # Create a set from list1 for O(1) lookup
    set1 = set(list1)
    
    # Iterate over elements in list2
    for element in list2:
        # Check if element is in set1
        if element in set1:
            common_elements.append(element)
    
    return common_elements