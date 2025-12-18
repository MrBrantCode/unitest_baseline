"""
QUESTION:
Implement a function `merge_sort` that sorts the elements of a list in ascending order in place. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the length of the input list. The implementation should not use any built-in sorting functions, libraries, or extra memory/data structures.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge(arr, left, right)
    
def merge(arr, left, right):
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