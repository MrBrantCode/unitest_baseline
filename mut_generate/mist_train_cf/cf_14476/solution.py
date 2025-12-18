"""
QUESTION:
Create a function called `merge_and_sort` that merges two lists by alternating elements, removes any duplicates, and returns the merged list in ascending order. The function should handle lists of different lengths, merging the shorter list first and appending the remaining elements from the longer list. The function should return a sorted list of unique integers.
"""

def merge_and_sort(list1, list2):
    merged_list = []
    i = 0
    j = 0
    
    # Alternate elements from both lists until one list is exhausted
    while i < len(list1) and j < len(list2):
        merged_list.append(list1[i])
        merged_list.append(list2[j])
        i += 1
        j += 1
    
    # Add remaining elements from the longer list
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
        
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    # Remove duplicates and sort the merged list
    merged_list = sorted(set(merged_list))
    
    return merged_list