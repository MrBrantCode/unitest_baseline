"""
QUESTION:
Write a function called `merge_sorted_lists` that takes two sorted lists as input and returns a new sorted list containing all elements from both input lists. The input lists may contain duplicate elements. The function must handle lists of varying lengths.
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