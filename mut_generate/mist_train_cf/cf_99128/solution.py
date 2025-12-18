"""
QUESTION:
Write a function named `common_elements` that takes two lists of integers as input and returns a list of their common elements. The function should have a time complexity that can handle lists with millions of elements and should handle edge cases, such as when one or both lists are empty, or when the lists contain duplicate elements.
"""

def common_elements(list1, list2):
    if not list1 or not list2:  # Check for empty lists
        return []
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    if len(common) == 0:  # Check for no common elements
        return []
    else:
        return list(common)