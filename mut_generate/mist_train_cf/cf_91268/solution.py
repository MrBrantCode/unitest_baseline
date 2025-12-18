"""
QUESTION:
Create a function named `find_common_elements` that takes two lists of integers as input and returns a new list containing the common elements from both input lists. The function should have a time complexity of O(n), where n is the length of the longer input list.
"""

def find_common_elements(list1, list2):
    # Create a set from the first list for O(1) lookup time
    set1 = set(list1)
    # Initialize an empty list to store the common elements
    common_elements = []
  
    # Iterate through the second list
    for num in list2:
        # Check if the current element exists in the first set
        if num in set1:
            # Add the common element to the common_elements list
            common_elements.append(num)

    return common_elements