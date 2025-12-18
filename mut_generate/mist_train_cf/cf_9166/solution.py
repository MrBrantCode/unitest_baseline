"""
QUESTION:
Implement a function `merge_sort(arr)` that takes an array of integers as input and returns the array sorted in decreasing order using only recursion and without any built-in sorting functions or loops. The function should be able to handle arrays with duplicate elements and have a time complexity of O(nlogn) and a space complexity of O(logn).
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] >= right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1
    
    result.extend(left_half[left_index:])
    result.extend(right_half[right_index:])
    
    return result