"""
QUESTION:
Write a function called `binary_search` that performs a binary search on a sorted array to find the index of a given target value. The function should be able to handle arrays sorted in ascending or descending order. If the target value is not present in the array, the function should return -1. If the target value has duplicates, the function should return the index of the first occurrence if the array is sorted in ascending order, and the index of the last occurrence if the array is sorted in descending order. The function should have a time complexity of O(log n).
"""

def binary_search(arr, target, is_ascending=True):
    def recursive_binary_search(arr, target, low, high, is_ascending):
        if low > high:
            return -1

        mid = (low + high) // 2

        if arr[mid] == target:
            if is_ascending:
                if mid > 0 and arr[mid - 1] == target:
                    return recursive_binary_search(arr, target, low, mid - 1, is_ascending)
                else:
                    return mid
            else:
                if mid < len(arr) - 1 and arr[mid + 1] == target:
                    return recursive_binary_search(arr, target, mid + 1, high, is_ascending)
                else:
                    return mid
        elif (is_ascending and arr[mid] > target) or (not is_ascending and arr[mid] < target):
            return recursive_binary_search(arr, target, low, mid - 1, is_ascending)
        else:
            return recursive_binary_search(arr, target, mid + 1, high, is_ascending)

    if is_ascending:
        return recursive_binary_search(arr, target, 0, len(arr) - 1, is_ascending)
    else:
        return recursive_binary_search(arr, target, 0, len(arr) - 1, is_ascending)