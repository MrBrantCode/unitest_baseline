"""
QUESTION:
Write a function named `find_common_elements` that takes two lists of integers as input and returns a new list containing their common elements. The function should have a time complexity of O(n+m), where n and m are the lengths of the two input lists, and it should not use any additional data structures other than the input lists and the output list.
"""

def find_common_elements(list1, list2):
    list1.sort()
    list2.sort()
    
    common_elements = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            common_elements.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
            
    return common_elements