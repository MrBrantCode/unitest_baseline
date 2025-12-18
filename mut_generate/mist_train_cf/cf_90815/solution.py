"""
QUESTION:
Write a function named `merge_sorted_lists` that merges two sorted lists, `list1` and `list2`, into a single sorted list. The lists can contain duplicate elements. The function should return the merged and sorted list. The function should handle lists of different lengths and lists that are already merged or in reverse order.
"""

def merge_sorted_lists(list1, list2):
    merged_list = []
    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(list1) and ptr2 < len(list2):
        if list1[ptr1] <= list2[ptr2]:
            merged_list.append(list1[ptr1])
            ptr1 += 1
        else:
            merged_list.append(list2[ptr2])
            ptr2 += 1

    while ptr1 < len(list1):
        merged_list.append(list1[ptr1])
        ptr1 += 1

    while ptr2 < len(list2):
        merged_list.append(list2[ptr2])
        ptr2 += 1

    return merged_list