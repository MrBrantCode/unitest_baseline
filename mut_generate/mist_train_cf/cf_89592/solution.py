"""
QUESTION:
Write a function named `get_unique_elements` that takes two lists `a` and `b` as input and returns a new list containing elements present in `a` but not in `b`, sorted in ascending order. The function should not use any built-in Python functions or libraries that directly solve this problem, have a time complexity of O(n log n), and should not modify the original input lists. The input lists can have a maximum length of 1000 elements each and may contain duplicate elements.
"""

def get_unique_elements(a, b):
    # Create a set from list b for faster lookup
    b_set = set(b)
    
    # Initialize an empty list to store unique elements
    unique_elements = []
    
    # Iterate through each element in list a
    for element in a:
        # Check if the element is not in set b
        if element not in b_set:
            # Add the element to the list of unique elements
            unique_elements.append(element)
    
    # Sort the list of unique elements in ascending order
    unique_elements.sort()
    
    # Return the list of unique elements
    return unique_elements