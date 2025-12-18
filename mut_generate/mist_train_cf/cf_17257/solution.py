"""
QUESTION:
Implement a function `merge_sort` that sorts a list of strings in alphabetical order from a-z with a time complexity of O(n log n) and handles case-insensitive sorting. The function should preserve the original order of elements if they have the same value when compared in a case-insensitive manner. Do not use the built-in sorting function or any sorting algorithm with a lower time complexity than O(n log n).
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result