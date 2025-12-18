"""
QUESTION:
Write a function `merge_sort(arr)` to implement the merge sort algorithm, which efficiently sorts a list of elements in ascending order. The function should take a list of elements as input and return the sorted list. 

The merge sort algorithm should follow these steps: 
1. Divide: Divide the original list into two halves.
2. Conquer: Recursively sort each half until the base case is reached (when the list has only one element).
3. Combine: Merge the sorted halves back together to produce the final sorted list.

Restrictions:
- Use a divide and conquer approach.
- The function should handle lists with any number of elements.
- The function should return the sorted list in ascending order.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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