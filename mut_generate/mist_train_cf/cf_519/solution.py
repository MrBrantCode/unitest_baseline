"""
QUESTION:
Implement a function `merge_sorted_lists` that merges two sorted lists into a single sorted list with unique elements. The function should have a time complexity of O(n+m), where n and m are the lengths of the two input lists respectively. The merged list should not contain any duplicate elements, and you are not allowed to use any additional data structures or libraries.
"""

def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

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
        if not merged_list or merged_list[-1] != list1[i]:
            merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        if not merged_list or merged_list[-1] != list2[j]:
            merged_list.append(list2[j])
        j += 1

    return merged_list