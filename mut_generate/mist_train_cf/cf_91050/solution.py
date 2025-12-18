"""
QUESTION:
Write a function named `find_common_elements` that takes two lists of unique integers as input, `set1` and `set2`, and returns a list of the common elements between the two lists, ensuring each element appears only once in the result. The solution must have a time complexity of O(n), where n is the total number of elements in both lists combined.
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