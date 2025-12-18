"""
QUESTION:
Write a function named `find_common_elements` that takes two lists `list1` and `list2` as arguments and returns the elements that are common to both lists in the same order as they appear in `list1`. The function should handle cases where the elements can be of different data types, ignore any duplicates within each list, and not use the built-in intersection operation or any other built-in function that directly solves the problem.
"""

def find_common_elements(list1, list2):
    element_counts = {}
    
    for element in list1:
        if element not in element_counts:
            element_counts[element] = 1
    
    common_elements = []
    
    for element in list2:
        if element in element_counts and element_counts[element] > 0:
            common_elements.append(element)
            element_counts[element] -= 1
    
    return common_elements