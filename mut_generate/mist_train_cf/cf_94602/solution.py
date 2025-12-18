"""
QUESTION:
Implement a function `merge_sort` that takes an integer list as its input and returns a sorted list. The function should have a time complexity of O(n log n) and a space complexity of O(n). The sorted list should contain all duplicate elements present in the input list, maintaining their relative order. Do not use any built-in sorting functions or libraries, and do not use additional data structures.
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