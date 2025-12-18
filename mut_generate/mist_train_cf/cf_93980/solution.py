"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array `arr` to find if the `target` exists in the array. The array may contain duplicates, and the function should be able to handle these duplicates correctly. The function should return a boolean indicating whether the target exists in the array or not.
"""

def entance(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True

        if arr[mid] == arr[left]:
            left += 1
        elif arr[mid] == arr[right]:
            right -= 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False