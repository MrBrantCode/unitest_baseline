"""
QUESTION:
Implement the `merge_sort` function to sort an array of strings in alphabetical order. The function should not use any built-in sorting functions and should have a time complexity of O(nlogn). The input array will contain only strings, and the output should be a sorted array of strings.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

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

    # Add remaining elements from the subarrays
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged