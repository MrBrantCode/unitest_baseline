"""
QUESTION:
Design a function `find_common_elements` that takes two sorted lists `list_one` and `list_two` as input and returns three values: a list of common elements, a list of indices of common elements in `list_one`, and a list of indices of common elements in `list_two`. The function should not use any built-in functions or libraries for searching or comparing elements in the lists and should handle duplicate elements. The function should implement its own algorithm for finding the common elements and their indices. The lists can contain duplicate elements and the common elements should be counted multiple times based on their occurrences in both lists.
"""

def find_common_elements(list_one, list_two):
    common_elements = []
    list_one_indices = []
    list_two_indices = []
    
    i = 0
    j = 0
    
    while i < len(list_one) and j < len(list_two):
        if list_one[i] < list_two[j]:
            i += 1
        elif list_one[i] > list_two[j]:
            j += 1
        else:
            common_elements.append(list_one[i])
            list_one_indices.append(i)
            list_two_indices.append(j)
            i += 1
            j += 1
    
    return common_elements, list_one_indices, list_two_indices