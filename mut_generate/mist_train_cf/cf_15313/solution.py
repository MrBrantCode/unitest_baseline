"""
QUESTION:
Write a function `find_consecutive_intersection(list1, list2)` that finds the intersection between two lists, where the elements in the intersection should appear in the same order as they appear in the first list. The function should only consider elements that occur consecutively in both lists, stopping as soon as a mismatch occurs. The function should take two lists of elements as input and return a list of the consecutive intersection elements.
"""

def find_consecutive_intersection(list1, list2):
    intersection = []
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            intersection.append(list1[i])
            i += 1
            j += 1
        else:
            i += 1
    
    return intersection