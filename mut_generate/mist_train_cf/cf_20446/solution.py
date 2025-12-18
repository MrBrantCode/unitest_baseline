"""
QUESTION:
Create a function named `merge_lists` that takes two sorted lists as input and returns a new sorted list that contains all unique elements from both lists in ascending order. The function should have a time complexity of O(n+m), where n and m are the lengths of the two input lists.
"""

def entance(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1
            j += 1
    
    while i < len(list1):
        if list1[i] not in merged_list:
            merged_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        if list2[j] not in merged_list:
            merged_list.append(list2[j])
        j += 1
    
    return sorted(merged_list)