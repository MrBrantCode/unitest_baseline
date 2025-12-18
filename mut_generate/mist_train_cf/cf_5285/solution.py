"""
QUESTION:
Implement a function `binary_search(nums, target)` that performs a binary search on a sorted array `nums` to find the index of the first occurrence of the target value. If the target is not found, return -1. Assume that the input array `nums` is sorted in ascending order and may contain duplicates. The function should have a time complexity of O(log n).
"""

def entrance(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            # Check if mid is the first occurrence of the target
            if mid == 0 or nums[mid - 1] != target:
                return mid
            else:
                # Continue searching on the left half
                high = mid - 1
        elif nums[mid] < target:
            # Continue searching on the right half
            low = mid + 1
        else:
            # Continue searching on the left half
            high = mid - 1

    # Target not found
    return -1