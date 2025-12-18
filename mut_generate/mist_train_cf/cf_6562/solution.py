"""
QUESTION:
Implement the `merge_sort` function, which takes an array of integers as input and returns a tuple containing the sorted array in ascending order and the number of comparisons made during the sorting process. The function must use a recursive approach, have a time complexity of O(nlogn), and handle duplicate values and negative integers. The function should be stable, maintaining the relative order of elements with equal values, and use constant space complexity (O(1)) for auxiliary data structures.
"""

def merge_sort(arr):
    comparisons = 0
    
    if len(arr) <= 1:
        return arr, comparisons
    
    mid = len(arr) // 2
    left, comparisons_left = merge_sort(arr[:mid])
    right, comparisons_right = merge_sort(arr[mid:])
    comparisons += comparisons_left + comparisons_right
    
    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        comparisons += 1
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
    
    return merged, comparisons