"""
QUESTION:
Implement the `merge_sort` function in Python, which takes an array of integers as input and sorts it in-place using the Merge Sort algorithm. The function must meet the following requirements:

- The sorting algorithm must have a time complexity of O(n log n).
- The sorting algorithm must not use any built-in sorting functions or libraries.
- The sorting algorithm must be able to handle large input sizes (e.g., an array with 10^6 elements).
- The sorting algorithm must be in-place, meaning it does not use additional memory proportional to the input size.
- The sorting algorithm must be adaptive, meaning it should take advantage of any pre-existing order in the data.
- The sorting algorithm must be able to handle duplicate elements in the data.
- The sorting algorithm must be stable, meaning it preserves the relative order of equal elements.
"""

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