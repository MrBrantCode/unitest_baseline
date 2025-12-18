"""
QUESTION:
Create a function named `find_common_elements` that takes two lists, `list1` and `list2`, as input and returns a list of common elements without any duplicates in descending order. The function should be able to handle lists with up to 100,000 elements and have a time complexity better than O(n^2).
"""

def find_common_elements(list1, list2):
    common_elements = set(list1)
    result = set()
    
    for element in list2:
        if element in common_elements:
            result.add(element)
    
    return sorted(result, reverse=True)