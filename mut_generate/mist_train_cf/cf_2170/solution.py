"""
QUESTION:
Implement a function named `merge_sort` that takes an array as input and returns the sorted array using the merge sort algorithm. The function should recursively divide the array into halves until it reaches a base case of length 1 or 0, then merge the sorted subarrays. 

The function should have a time complexity of O(n log n) and a space complexity of O(n). However, you can propose an optimization to reduce the space complexity to O(1) by implementing an "In-place Merge Sort".
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result