"""
QUESTION:
Create a function named `merge_and_remove_duplicates` that takes two sorted lists as input and returns a new sorted list that contains all unique elements from both input lists. The function should have a time complexity of O(n+m), where n and m are the lengths of the two input lists. The returned list should be sorted in ascending order.
"""

def merge_and_remove_duplicates(list1, list2):
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
        merged_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    # Remove duplicates
    merged_list = list(set(merged_list))
    
    # Sort the merged list
    merged_list.sort()
    
    return merged_list