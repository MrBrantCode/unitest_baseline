"""
QUESTION:
Create a function named `merge_sort` that takes an array of integers as input. The function should sort the array in ascending order, have a time complexity of O(n log n), and a space complexity of O(1). The function should sort the array in-place, modifying the original array.
"""

def merge_sort(arr):
    def merge(left, right):
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge(left, right)