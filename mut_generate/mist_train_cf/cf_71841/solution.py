"""
QUESTION:
Implement a function `rotated_array_search(arr, target)` that finds the index of a target element within a sorted and rotated array. The function should return the index of the target element if found, and -1 otherwise. The time complexity of the function should be O(log n).
"""

def rotated_array_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= arr[left]:
            if target >= arr[left] and target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target <= arr[right] and target > arr[mid]: 
                left = mid + 1
            else:
                right = mid - 1
    return -1