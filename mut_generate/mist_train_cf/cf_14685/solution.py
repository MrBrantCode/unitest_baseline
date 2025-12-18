"""
QUESTION:
Write a function `find_common_elements(list1, list2)` that takes two lists as input and returns a set of common elements between them. The function should have a time complexity of O(n), where n is the length of the longer list. The function should handle lists of any length, including empty lists, and the order of elements in the output set does not matter. The function should not use built-in functions or methods that directly compare lists or convert lists to sets.
"""

def find_common_elements(list1, list2):
    # Create a set to store the common elements
    common_elements = set()
    
    # Iterate through the elements of list1
    for element in list1:
        # Check if the element is in list2
        if element in list2:
            # Add the element to the common_elements set
            common_elements.add(element)
    
    return common_elements