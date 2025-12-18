"""
QUESTION:
Implement a function called `merge_sort` that sorts an array of integers in ascending order using a stable sorting algorithm with a time complexity of O(nlogn). The function should not use any built-in sorting functions or libraries and should correctly handle duplicate values, preserving their relative order in the original array.
"""

def merge_sort(arr):
    def merge(left, right):
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1
        
        return merged
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)