"""
QUESTION:
Implement the `merge_sort` function, which sorts an array of integers using the Merge Sort algorithm. The function should divide the array into two halves until each sub-array contains a single element, then merge the sub-arrays in a sorted manner. Use recursion to divide and merge the array. The function should return the sorted array.
"""

def merge_sort(arr):
    # base case: if array has one or zero elements, it's already sorted
    if len(arr) <= 1: 
        return arr

    # divide array into two halves
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # merge two halves (while sorting them)
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # merging happens here
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # if any element was left
    merged += left[left_index:]
    merged += right[right_index:]

    return merged