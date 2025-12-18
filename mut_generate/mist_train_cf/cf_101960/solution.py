"""
QUESTION:
Write a Python function `common_elements` that takes two lists of integers as input and returns a new list containing only the common elements between the two input lists. The function should have a time complexity of O(nlogn), where n is the length of the longer input list. The order of the common elements in the output list should be the same as the order they appear in the sorted input lists.
"""

def common_elements(list1, list2):
    list1.sort()  
    list2.sort()  
    
    common = []  
    
    i = 0  
    j = 0  
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            common.append(list1[i])
            i += 1
            j += 1
            
    return common