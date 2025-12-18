"""
QUESTION:
Write a function named `find_consecutive_intersection` that takes two lists as input and returns a list containing the consecutive intersection of the two input lists, with elements in the same order as they appear in the first list. The function should only consider elements that occur consecutively in both lists.
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