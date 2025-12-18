"""
QUESTION:
Find the most common elements between two sets with a time complexity of O(n), where n is the total number of elements in both sets. The function should ensure that each element appears only once in the final result and return the common elements in a list. The function should be named "find_common_elements" and take two parameters, "set1" and "set2", which are lists of elements.
"""

def find_common_elements(set1, set2):
    common_elements = set()
    result = []
    
    for element in set1:
        common_elements.add(element)
    
    for element in set2:
        if element in common_elements:
            common_elements.remove(element)
            result.append(element)
    
    return result