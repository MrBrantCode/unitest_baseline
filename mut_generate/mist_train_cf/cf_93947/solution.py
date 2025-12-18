"""
QUESTION:
Create a function `find_common_elements` that takes two lists of integers `list1` and `list2` as input. The function should return all unique common elements from both lists in ascending order, along with the count of these common elements. The input lists can contain both positive and negative integers, with a maximum length of 1000 elements. The function should not use any built-in Python functions or methods for finding common elements or sorting, and its time complexity should be O(n), where n is the total number of elements in both lists.
"""

def find_common_elements(list1, list2):
    # Create empty dictionaries to store the unique elements and their counts
    elements1 = {}
    elements2 = {}
    
    # Iterate over the elements in list1
    for element in list1:
        # If the element is not in the dictionary, add it with a count of 1
        if element not in elements1:
            elements1[element] = 1
        # If the element is already in the dictionary, increment its count
        else:
            elements1[element] += 1
    
    # Iterate over the elements in list2
    for element in list2:
        # If the element is not in the dictionary, add it with a count of 1
        if element not in elements2:
            elements2[element] = 1
        # If the element is already in the dictionary, increment its count
        else:
            elements2[element] += 1
    
    # Create an empty list to store the common elements
    common_elements = []
    
    # Iterate over the elements in list1
    for element in elements1:
        # If the element is in both dictionaries, it is a common element
        if element in elements2:
            # Add the element to the common_elements list as many times as the minimum count in the two dictionaries
            common_elements.extend([element] * min(elements1[element], elements2[element]))
    
    # Sort the common_elements list in ascending order
    common_elements.sort()
    
    # Return the common_elements list and its count
    return common_elements, len(common_elements)