"""
QUESTION:
Write a function named `merge_lists` that merges two sorted lists of numbers, removes any duplicates, and maintains the sorted order. The function should handle cases where one or both of the lists contain negative numbers and run in O(n) time complexity.
"""

def merge_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if merged_list and merged_list[-1] == list2[j]:
                j += 1
            else:
                merged_list.append(list2[j])
                j += 1
        else:
            if merged_list and merged_list[-1] != list1[i]:
                merged_list.append(list1[i])
            i += 1
            j += 1
    
    while i < len(list1):
        if merged_list and merged_list[-1] == list1[i]:
            i += 1
        else:
            merged_list.append(list1[i])
            i += 1
    
    while j < len(list2):
        if merged_list and merged_list[-1] == list2[j]:
            j += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    return merged_list