"""
QUESTION:
Implement the merge_sort function to sort an array of integers in ascending order using the merge sort algorithm. The function should take an array as input and return the sorted array. The merge sort algorithm should divide the array into equally sized subarrays until each subarray contains only one element, and then merge the subarrays in a way that they become sorted.
"""

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    left_half = array[:len(array) // 2]
    right_half = array[len(array) // 2:]
    
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
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