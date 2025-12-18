"""
QUESTION:
Implement a function named `binary_search_multi` that takes a list of integers `arr` and a target integer `target` as input. The function should return the starting and ending indices of the `target` in the sorted `arr`. If the `target` is not found in `arr`, the function should return -1. Assume that the input list `arr` may contain duplicate elements. The function should have a time complexity of O(n log n) due to sorting and O(log n) for the binary search.
"""

def binary_search_multi(arr, target):
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Augment the array with the starting and ending indices of each key
    augmented_arr = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            augmented_arr.append((arr[i], i, i))
        else:
            augmented_arr[-1] = (augmented_arr[-1][0], augmented_arr[-1][1], i)
            
    # Perform binary search on the augmented array
    left, right = 0, len(augmented_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if augmented_arr[mid][0] == target:
            return augmented_arr[mid][1], augmented_arr[mid][2]
        elif augmented_arr[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    # Target key not found in the array
    return -1