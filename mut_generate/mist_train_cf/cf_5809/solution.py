"""
QUESTION:
Create a function called `merge_lists` that takes two sorted lists, `list1` and `list2`, as input and returns a new sorted list that contains all elements from both lists without duplicates. The function should have a time complexity of O(n+m), where n and m are the lengths of `list1` and `list2` respectively. The returned list should be sorted in ascending order.
"""

def merge_lists(list1, list2):
    i = j = 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not merged_list or merged_list[-1] != list1[i]:
                merged_list.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
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