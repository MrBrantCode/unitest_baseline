"""
QUESTION:
Write a function `get_overlapping_elements(list1, list2)` that returns a list of overlapping elements between two input lists, considering both flat and nested lists. The function should handle duplicates and nested lists of arbitrary depth.
"""

def get_overlapping_elements(list1, list2):
    overlapping_elements = []
    for item in list1:
        if item in list2:
            overlapping_elements.append(item)
        if isinstance(item, list):
            overlapping_elements.extend(get_overlapping_elements(item, list2))
    return overlapping_elements