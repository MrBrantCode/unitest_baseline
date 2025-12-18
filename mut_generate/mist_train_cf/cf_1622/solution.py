"""
QUESTION:
Implement a function called merge_sort(arr) that sorts an array in ascending order, handles duplicate elements, and maintains the relative order of elements with equal keys. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left_half = arr[0 : len(arr)//2]
    right_half = arr[len(arr)//2 : ]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    sorted_arr = []
    i = 0
    j = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1
    
    while i < len(left_half):
        sorted_arr.append(left_half[i])
        i += 1
    
    while j < len(right_half):
        sorted_arr.append(right_half[j])
        j += 1
    
    return sorted_arr