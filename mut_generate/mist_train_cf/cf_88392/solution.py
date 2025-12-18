"""
QUESTION:
Implement the function `merge_sort(arr)` to sort the elements in an integer array `arr` in non-decreasing order using constant space complexity without built-in sorting functions or libraries. The function should have a time complexity of O(n log n) or better and handle arrays with repeated elements efficiently. The length of the array will be between 1 and 1000, and each element will be between -10^9 and 10^9.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    left_ptr = right_ptr = 0
    
    while left_ptr < len(left_half) and right_ptr < len(right_half):
        if left_half[left_ptr] <= right_half[right_ptr]:
            merged.append(left_half[left_ptr])
            left_ptr += 1
        else:
            merged.append(right_half[right_ptr])
            right_ptr += 1
    
    # Append remaining elements from either half
    merged.extend(left_half[left_ptr:])
    merged.extend(right_half[right_ptr:])
    
    return merged