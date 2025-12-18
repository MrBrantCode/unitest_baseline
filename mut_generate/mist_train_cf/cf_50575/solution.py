"""
QUESTION:
Write a function named `merge_sorted_lists` that merges two sorted lists into one sorted list without using the built-in sort function or any third-party libraries. The function should also remove any duplicate values from the merged list. The input lists are assumed to be sorted in ascending order.
"""

def merge_sorted_lists(list1, list2):
    i = j = 0
    merged_list = []
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if list1[i] not in merged_list:
                merged_list.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
            if list2[j] not in merged_list:
                merged_list.append(list2[j])
            j += 1
        else:
            if list1[i] not in merged_list:
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
    return merged_list