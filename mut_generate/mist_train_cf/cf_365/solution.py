"""
QUESTION:
Implement a function named `merge_sort` that sorts an array in descending order using a divide and conquer approach with recursion. The function should have a time complexity of O(nlogn) and an auxiliary space complexity of O(logn). It should not use any built-in sorting functions or data structures. The original array should remain unchanged, and the sorted array should be stored in a new array.
"""

def merge_sort(arr):
    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0
        
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        
        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1
        
        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1
        
        return merged

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)