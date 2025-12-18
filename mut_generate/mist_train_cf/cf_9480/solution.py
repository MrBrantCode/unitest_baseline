"""
QUESTION:
Create a function named `find_common_elements` that takes two lists of integers as input. Each list can contain both positive and negative integers and can have a maximum length of 1000 elements. The function should return a tuple containing the common elements in ascending order with duplicates removed and the count of common elements.
"""

def find_common_elements(list1, list2):
    # Remove duplicates from both lists
    list1 = list(set(list1))
    list2 = list(set(list2))
    
    # Find common elements
    common_elements = sorted(list(set(list1) & set(list2)))
    
    # Count of common elements
    count = len(common_elements)
    
    return common_elements, count