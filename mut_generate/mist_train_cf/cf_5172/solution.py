"""
QUESTION:
Implement the merge_sort function that takes an array of integers as input and sorts it in-place without using any extra data structures or libraries. The function should have a time complexity of O(nlogn) and be able to handle large arrays efficiently. Additionally, the function should be stable, meaning that the relative order of equal elements should be preserved after sorting. The array can contain positive and negative integers.
"""

def entrance(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    entrance(left_half)
    entrance(right_half)
    
    merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1