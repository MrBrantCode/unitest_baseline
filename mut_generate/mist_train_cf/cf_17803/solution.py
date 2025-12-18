"""
QUESTION:
Create a function `common_elements(list1, list2)` that takes two lists of integers as input and returns a list of integers that are common in both lists. The function should have a time complexity of O(n), where n is the length of the longer list. The input lists can contain duplicates and the order of elements in the resulting list does not matter.
"""

def common_elements(list1, list2):
    # Create a set from one of the lists for O(1) lookup
    set1 = set(list1)
    
    # Initialize an empty list to store the common elements
    common = []
    
    # Iterate through the elements in list2
    for num in list2:
        # Check if the element is in set1
        if num in set1:
            # If it is, append it to the common list
            common.append(num)
    
    # Return the common list
    return common