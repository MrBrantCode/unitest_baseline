"""
QUESTION:
Create a function called `merge_lists` that takes two sorted lists of numbers as input. The function should merge the two lists and remove any duplicates while maintaining the sorted order. The function should also handle cases where one or both of the lists contain negative numbers and run in O(n) time complexity.
"""

def merge_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not merged_list or merged_list[-1] != list1[i]:
                merged_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not merged_list or merged_list[-1] != list2[j]:
                merged_list.append(list2[j])
            j += 1
        else:
            if not merged_list or merged_list[-1] != list1[i]:
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