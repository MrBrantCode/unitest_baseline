"""
QUESTION:
Write a function named `find_common_elements` that takes two lists, `list1` and `list2`, as arguments. The function should return the elements that are common to both lists, ignoring any duplicates within each list and maintaining the same order as they appear in `list1`. The function should handle cases where the elements can be of different data types and should not use any built-in intersection operation or other functions that directly solve the problem.
"""

def entance(list1, list2):
    # Create a dictionary to keep track of the elements in list1
    element_counts = {}
    
    # Loop through each element in list1 and add it to the dictionary
    for element in list1:
        # Ignore duplicates by checking if the element is already in the dictionary
        if element not in element_counts:
            element_counts[element] = 1
    
    # Create a list to store the common elements
    common_elements = []
    
    # Loop through each element in list2
    for element in list2:
        # Check if the element is in the dictionary and if its count is greater than 0
        if element in element_counts and element_counts[element] > 0:
            # Add the element to the common_elements list
            common_elements.append(element)
            # Decrement the count of the element in the dictionary
            element_counts[element] -= 1
    
    # Return the common elements in the same order as they appear in list1
    return common_elements