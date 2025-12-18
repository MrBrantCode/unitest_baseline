"""
QUESTION:
Implement a function `merge_sort(lst)` that sorts a list of numbers in ascending order while preserving the relative order of duplicate numbers. The function should have a time complexity of O(n log n).
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])
    
    merged = []
    i = 0
    j = 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    
    # Append remaining elements
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    
    return merged