"""
QUESTION:
Implement a function `find_overlapping_elements(list1, list2)` that finds and returns the overlapping elements between two lists `list1` and `list2`. The lists can contain duplicates and nested lists, which may contain further nested lists. The function should consider these nested lists when finding overlapping elements.
"""

def find_overlapping_elements(list1, list2):
    result = []
    
    # Iterate over elements in list1
    for item in list1:
        # Check if item is also present in list2
        if item in list2:
            result.append(item)
        # Check if item is a list
        if isinstance(item, list):
            # Recursively call the function for the nested list
            nested_result = find_overlapping_elements(item, list2)
            # Extend the result list with the nested result
            result.extend(nested_result)
    
    return result