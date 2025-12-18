"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array `arr` to find the `target` element. The function should handle duplicate elements in the array and return `True` if the `target` is found, `False` otherwise.
"""

def entance(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True

        # Check if the mid element is the same as the left element
        # If so, move the left pointer to skip the duplicate
        if arr[mid] == arr[left]:
            left += 1
        # Check if the mid element is the same as the right element
        # If so, move the right pointer to skip the duplicate
        elif arr[mid] == arr[right]:
            right -= 1
        # Check if the target is less than the mid element
        # If so, search the left half of the array
        elif target < arr[mid]:
            right = mid - 1
        # Otherwise, search the right half of the array
        else:
            left = mid + 1

    return False