"""
QUESTION:
Create a function named `merge_arrays` that takes two arrays as input, merges them into one array, sorts the resulting array in ascending order, removes any duplicate elements, and returns the resulting array. The original arrays should remain unchanged and the function should achieve a time complexity of O(n log n) without using any built-in sorting functions or data structures.
"""

def merge_arrays(array1, array2):
    merged_array = array1 + array2
    sorted_array = merge_sort(merged_array)
    final_array = remove_duplicates(sorted_array)
    return final_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        elif left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
            j += 1
            
    while i < len(left):
        merged.append(left[i])
        i += 1
        
    while j < len(right):
        merged.append(right[j])
        j += 1
        
    return merged

def remove_duplicates(arr):
    if len(arr) <= 1:
        return arr
    
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    
    return result