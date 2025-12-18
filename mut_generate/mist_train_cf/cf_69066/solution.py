"""
QUESTION:
Write a function `search(nums, target)` that takes a rotated sorted array `nums` and an integer `target` as inputs, and returns the index of `target` if it exists in `nums`, or `-1` if it doesn't. The array `nums` is initially sorted in ascending order with unique values and is rotated at an unknown pivot index. The length of `nums` is between 1 and 5000 (inclusive), and all values in `nums` are between -10^4 and 10^4 (inclusive). The target value is also between -10^4 and 10^4 (inclusive). The function should achieve a time complexity of O(log n).
"""

def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:    # Left side is sorted
            if nums[low] <= target and target < nums[mid]:   # Target is in the left half
                high = mid - 1
            else:
                low = mid + 1
        else:    # Right side is sorted
            if nums[mid] < target and target <= nums[high]:  # Target is in the right half
                low = mid + 1
            else:
                high = mid - 1
    return -1