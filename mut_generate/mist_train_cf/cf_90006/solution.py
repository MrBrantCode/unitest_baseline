"""
QUESTION:
Write a recursive function named `find_target_index` that finds the index of the first occurrence of a target value in a sorted array of integers. The function should take four parameters: the array, the target value, and the start and end indices. The function should return the index of the target value if found, and -1 otherwise. The function should have a time complexity of O(log n).
"""

def find_target_index(arr, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return find_target_index(arr, target, start, mid - 1)
    
    else:
        return find_target_index(arr, target, mid + 1, end)