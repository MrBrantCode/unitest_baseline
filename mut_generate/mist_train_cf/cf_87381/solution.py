"""
QUESTION:
Implement the function merge_sort(arr) that takes an array of integers as input and sorts the array in ascending order using a stable sorting algorithm with a time complexity of O(n log n). The algorithm must not use any built-in sorting functions or libraries, must be in-place, adaptive, and able to handle large input sizes, duplicate elements, and preserve the relative order of equal elements.
"""

def merge_sort(arr):
    def merge(left, right, arr):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
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
    
    merge(left, right, arr)