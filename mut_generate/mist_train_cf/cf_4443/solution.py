"""
QUESTION:
Implement a function `merge_sort` that takes an array of strings as input and returns the sorted array. The sorting should be done based on the length of the strings in descending order. If two strings have the same length, they should be sorted lexicographically in descending order. The implementation should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if (len(left_half[i]), left_half[i]) > (len(right_half[j]), right_half[j]):
            arr[i + j] = left_half[i]
            i += 1
        else:
            arr[i + j] = right_half[j]
            j += 1
    
    while i < len(left_half):
        arr[i + j] = left_half[i]
        i += 1
    
    while j < len(right_half):
        arr[i + j] = right_half[j]
        j += 1
    
    return arr