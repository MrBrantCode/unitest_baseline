"""
QUESTION:
Write a function named `find_intersecting_elements` that takes three lists of integers as input, finds their intersecting elements considering only unique values, and returns these intersecting elements in descending order. The function should have a near-linear time complexity, O(n), where n is the length of the longest list.
"""

def find_intersecting_elements(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    intersecting_elements = set1 & set2 & set3
    sorted_elements = sorted(intersecting_elements, reverse=True)
    
    return sorted_elements