"""
QUESTION:
Implement a function `binary_search(nums, target)` that uses the binary search algorithm to find the index of the first occurrence of the target in a sorted array `nums` with a time complexity of O(log n). The array `nums` is sorted in ascending order and may contain duplicates. If the target is not found, return -1.
"""

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target:
                return mid
            else:
                high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1