"""
QUESTION:
Write a function `find_duplicates` that takes a list of elements as input and returns a list of elements that appear more than once in the input list. The output list should be in ascending order and should not contain any duplicate elements. The function should not use any built-in functions or libraries. The input list will have a maximum length of 10^5.
"""

def find_duplicates(arr):
    # Create an empty set to store unique elements
    unique_elements = set()
    
    # Create an empty list to store duplicate elements
    duplicates = []
    
    # Iterate through each element in the input array
    for element in arr:
        # Check if the element is already in the unique_elements set
        if element in unique_elements:
            # Add the element to the duplicates list if it's not already in there
            if element not in duplicates:
                duplicates.append(element)
        else:
            # Add the element to the unique_elements set
            unique_elements.add(element)
    
    # Sort the duplicates list in ascending order
    duplicates.sort()
    
    return duplicates