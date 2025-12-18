"""
QUESTION:
Create a function called `merge_sort` to sort a list of numbers in ascending order while maintaining the relative order of duplicate numbers. The function should have a time complexity of O(n log n).
"""

def entrance(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    lst1 = entrance(lst[:mid])
    lst2 = entrance(lst[mid:])
    
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