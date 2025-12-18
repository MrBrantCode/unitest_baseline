"""
QUESTION:
Create a function called `find_common_elements` that takes two lists of integers, each with a maximum length of 1000, as input and returns a tuple containing a list of common elements in ascending order and the count of common elements. The function should ignore duplicate elements within each list.
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