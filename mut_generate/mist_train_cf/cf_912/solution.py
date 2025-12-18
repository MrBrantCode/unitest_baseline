"""
QUESTION:
Implement a function called `binary_search_duplicates` that takes a sorted array `arr` and a target value `target` as input. The function should return `True` if the target exists in the array and `False` otherwise. The function should handle duplicate elements in the array, have a time complexity of O(log n), and a space complexity of O(1).
"""

def binary_search_duplicates(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True

        if arr[mid] == arr[left] == arr[right]:
            left += 1
            right -= 1

        elif arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False