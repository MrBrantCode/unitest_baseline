"""
QUESTION:
Write a function `find_common_elements(list1, list2)` that takes two sorted lists as input and returns the elements that are present in both lists. The function should not use any built-in functions or methods for comparing or iterating through the lists, and should only use basic operations like indexing and arithmetic operations. The lists may contain duplicates and can have different lengths.
"""

def entance(list1, list2):
    i = 0
    j = 0
    common_elements = []
    
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