"""
QUESTION:
Implement a function named merge_sort that takes an array of integers as input and returns a new array with the same integers sorted in descending order. The function should have a time complexity of O(n log n), where n is the length of the array, and it should use a constant amount of extra space. The original array should not be modified during the sorting process.
"""

def merge_sort(arr):
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    merged_arr = merge(left_half, right_half)
    
    return merged_arr

def merge(left_arr, right_arr):
    merged = []
    left_index, right_index = 0, 0
    
    # Compare elements from both arrays and add them to the merged array in descending order
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] >= right_arr[right_index]:
            merged.append(left_arr[left_index])
            left_index += 1
        else:
            merged.append(right_arr[right_index])
            right_index += 1
    
    # Add any remaining elements from the left array
    while left_index < len(left_arr):
        merged.append(left_arr[left_index])
        left_index += 1
    
    # Add any remaining elements from the right array
    while right_index < len(right_arr):
        merged.append(right_arr[right_index])
        right_index += 1
    
    return merged