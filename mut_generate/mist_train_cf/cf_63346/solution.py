"""
QUESTION:
Implement the function `binary_search(nums, val)` that performs a binary search on a sorted list `nums` to find the index of the target value `val`. The function should take two arguments: `nums`, a sorted list of elements, and `val`, the value to be found. If the target value is found, the function should return its index; otherwise, it should return -1.
"""

def binary_search(nums, val):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    return -1