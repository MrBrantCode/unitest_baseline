"""
QUESTION:
Implement a function `merge_sort` that sorts a list of tuples in ascending order based on the first element of each tuple, where each tuple contains a number and its square. The function should have a time complexity of O(n log n) and a space complexity of O(n). The input list is a list of tuples where each tuple contains a number and its square, and the numbers are initially in random order. The function should not use any built-in sorting functions or libraries.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(arr, left, right)

def merge(arr, left, right):
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
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
    
    return arr