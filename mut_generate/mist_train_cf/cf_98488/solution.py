"""
QUESTION:
Implement a function named binary_search_multi that takes a list of integers and a target integer as input, and returns the starting and ending indices of the target integer in the list. If the target integer is not found, return -1. The function should have a time complexity of O(log n) and a space complexity of O(n).
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