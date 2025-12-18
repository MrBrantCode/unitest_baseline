"""
QUESTION:
Implement a function named merge_sort that sorts a list of integers in descending order, removes any duplicate values, and has a time complexity of O(nlogn) without using any built-in sorting functions or libraries. The input list contains integers and the function should return a new list containing the sorted integers in descending order without duplicates.
"""

def merge_sort(arr):
    arr = list(set(arr))  # remove duplicates
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(right[j])
            j += 1
        else:
            i += 1
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result