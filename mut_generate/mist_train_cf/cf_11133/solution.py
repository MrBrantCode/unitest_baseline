"""
QUESTION:
Implement a function called `merge_sort` that sorts an array of numbers in increasing order with a time complexity of O(n log n) and a constant space complexity. The function should take one argument: an array of numbers.
"""

def merge_sort(arr):
    n = len(arr)
    
    # Start with subarrays of size 1
    subarray_size = 1
    
    # Iterate over increasing subarray sizes
    while subarray_size < n:
        # Merge adjacent subarrays
        for left in range(0, n, subarray_size * 2):
            # Calculate the mid and right indices
            mid = min(left + subarray_size, n)
            right = min(left + subarray_size * 2, n)
            
            # Merge the subarrays
            arr[left:right] = merge(arr[left:mid], arr[mid:right])
        
        # Double the subarray size
        subarray_size *= 2
    
    return arr


def merge(left, right):
    result = []
    left_index = right_index = 0
    
    # Merge the two sorted halves
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Append the remaining elements
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result