"""
QUESTION:
Write a function `optimized_sort(arr)` that takes an array `arr` as input and returns a new array with the elements sorted in ascending order, without any duplicates. The sorting algorithm used should have a time complexity of O(n log n) and a space complexity of O(1) excluding the space required for the output array. You are not allowed to use any built-in sorting functions or libraries.
"""

def optimized_sort(arr):
    # Remove duplicates from the array
    arr = list(set(arr))
    
    # Implement merge sort algorithm to sort the array
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(optimized_sort(left_half), optimized_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged