"""
QUESTION:
Implement a function named `sort_descending` that takes a list of integers as input and returns the list sorted in descending order. The sorting algorithm should have a time complexity of O(n log n) and be stable, preserving the original order of equal elements. The function should be able to handle large input lists efficiently. Do not use any built-in sorting functions or methods.
"""

def sort_descending(arr):
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
    
    return merge_sort(arr)[::-1]