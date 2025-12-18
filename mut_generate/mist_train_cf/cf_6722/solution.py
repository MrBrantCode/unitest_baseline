"""
QUESTION:
Write a function `find_overlapping_elements(list1, list2)` that takes two lists as input and returns a new list containing the overlapping elements, including any nested lists. The function should handle lists that contain duplicates and nested lists of arbitrary depth.
"""

def entrance(list1, list2):
    result = []
    
    # Iterate over elements in list1
    for item in list1:
        # Check if item is also present in list2
        if item in list2:
            result.append(item)
        # Check if item is a list
        if isinstance(item, list):
            # Recursively call the function for the nested list
            nested_result = entrance(item, list2)
            # Extend the result list with the nested result
            result.extend(nested_result)
    
    return result