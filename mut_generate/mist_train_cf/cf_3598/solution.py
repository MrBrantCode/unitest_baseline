"""
QUESTION:
Write a Python function named `merge_sorted_lists` that takes in two sorted lists as input and returns a single merged list in ascending order. The merged list should contain unique elements only, i.e., if an element is present in both lists, it should only appear once in the merged list.
"""

def merge_sorted_lists(list1, list2):
    merged_list = []
    index1, index2 = 0, 0

    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            if list1[index1] not in merged_list:
                merged_list.append(list1[index1])
            index1 += 1
        elif list2[index2] < list1[index1]:
            if list2[index2] not in merged_list:
                merged_list.append(list2[index2])
            index2 += 1
        else:
            if list1[index1] not in merged_list:
                merged_list.append(list1[index1])
            index1 += 1
            index2 += 1

    while index1 < len(list1):
        if list1[index1] not in merged_list:
            merged_list.append(list1[index1])
        index1 += 1

    while index2 < len(list2):
        if list2[index2] not in merged_list:
            merged_list.append(list2[index2])
        index2 += 1

    return merged_list