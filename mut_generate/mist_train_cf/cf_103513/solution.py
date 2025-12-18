"""
QUESTION:
Create a function `find_intersecting_elements` that takes two lists of integers as input and returns a list of integers that are common to both input lists. The function should have a time complexity of O(nlogn) or better. The input lists may contain duplicate elements.
"""

def find_intersecting_elements(list1, list2):
    list1.sort()
    list2.sort()
    result = []
    pointer1 = 0
    pointer2 = 0
    
    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1] == list2[pointer2]:
            result.append(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif list1[pointer1] < list2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
    
    return result