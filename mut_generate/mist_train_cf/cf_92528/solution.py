"""
QUESTION:
Create a function called `merge_and_remove_duplicates` that takes two sorted lists `list1` and `list2` as input, merges them into a single sorted list in ascending order, and removes any duplicates. The function should have a time complexity of O(n+m), where n and m are the lengths of the input lists.
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