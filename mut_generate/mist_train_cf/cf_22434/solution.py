"""
QUESTION:
Implement the `merge_sort` function to sort a list of integers in ascending order, without using any built-in sorting functions or libraries, with a time complexity of O(n log n) and a space complexity of O(1). The function should take a list `arr` as input and return the sorted list.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result