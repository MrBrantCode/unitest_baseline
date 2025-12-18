"""
QUESTION:
Write a function named `find_common_elements` that compares two sorted lists and returns the elements that are present in both lists without using any built-in functions or methods for comparing or iterating through the lists. The lists may contain duplicates and can have different lengths. The function should use basic operations like indexing and arithmetic operations only.
"""

def find_common_elements(list1, list2):
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