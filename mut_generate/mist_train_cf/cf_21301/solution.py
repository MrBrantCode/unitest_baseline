"""
QUESTION:
Write a function `get_overlapping_elements(list1, list2)` that finds the overlapping elements between two lists, considering both single elements and nested lists. The function should handle duplicate elements and return a list of overlapping elements.
"""

def get_overlapping_elements(list1, list2):
    overlapping_elements = []
    for item in list1:
        if item in list2:
            overlapping_elements.append(item)
        if isinstance(item, list):
            overlapping_elements.extend(get_overlapping_elements(item, list2))
    return overlapping_elements