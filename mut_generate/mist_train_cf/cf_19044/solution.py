"""
QUESTION:
Create a function called merge_sort that takes an array of integers as input and returns the array sorted in non-decreasing order. The function should use constant space complexity, not use any built-in sorting functions or libraries, and have a time complexity of O(n log n) or better. The array will contain between 1 and 1000 elements, each ranging from -10^9 to 10^9.
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
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result