"""
QUESTION:
Implement a function named `merge_sort_descending` that sorts a list of integers in descending order using a time complexity of O(n log n) or better without using any built-in sorting functions or libraries. The function should be space efficient, using constant extra space, and stable, preserving the relative order of equal elements. The function should also handle large input sizes efficiently and allow for duplicate elements, placing duplicates together in the sorted output with the highest duplicates appearing first.
"""

def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_descending(arr[:mid])
    right = merge_sort_descending(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result