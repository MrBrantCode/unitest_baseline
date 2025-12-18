"""
QUESTION:
Create a function `merge_lists` that merges two sorted lists into a single sorted list, where the lists can contain duplicate elements. The function should have a time complexity of O(n+m), where n and m are the lengths of the two input lists respectively.
"""

def merge_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:  # both elements are equal
            merged_list.append(list1[i])
            merged_list.append(list2[j])
            i += 1
            j += 1

    # Add remaining elements from list1 (if any)
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Add remaining elements from list2 (if any)
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list