"""
QUESTION:
Design a function named `find_common_elements` that takes two sorted lists of integers as input and returns a list of their common elements. The function should not use built-in functions or libraries and should have a time complexity better than O(n^2), where n is the length of the input lists.
"""

def find_common_elements(list1, list2):
    common = []

    p1 = 0  # pointer for list1
    p2 = 0  # pointer for list2

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            p1 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:  
            common.append(list1[p1])
            p1 += 1
            p2 += 1

    return common