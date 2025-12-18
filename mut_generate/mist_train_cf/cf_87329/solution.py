"""
QUESTION:
Implement a function called `merge_sort` that sorts an array of integers in ascending order using the merge sort algorithm. The function should take an array as input and return a new sorted array. The function should divide the input array into halves until it reaches a base case of length 1 or 0, then merge the sorted subarrays back together in sorted order. Do not modify the original array and create a new array to store the sorted result. 

The function should also have a helper function called `merge` that merges two sorted subarrays into a single sorted array. 

The time complexity of the `merge_sort` function should be O(n log n) and the space complexity should be O(n), where n is the number of elements in the input array.
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