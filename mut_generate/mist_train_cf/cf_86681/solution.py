"""
QUESTION:
Implement a function `binary_search_duplicates(arr, target)` that performs a binary search on a sorted array `arr` to find the presence of a `target` element. The array may contain duplicates, and the function should have a time complexity of O(log n) and a space complexity of O(1).
"""

def binary_search_duplicates(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # If the middle element is the target
        if arr[mid] == target:
            return True

        # Check if the middle element is a duplicate
        if arr[mid] == arr[left] == arr[right]:
            left += 1
            right -= 1

        # If the left side is sorted
        elif arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # If the right side is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False