"""
QUESTION:
Implement a function named `search_last` that finds the last occurrence of a target number in a rotated sorted array. The function should take as input a list of integers `nums` and a target integer `target`. If the target is not found in the array, return -1. The function should use a helper function named `binary_search` to perform the search. The array is considered rotated if it was initially sorted in ascending order but was rotated at some point.
"""

def search_last(nums, target):
    if len(nums) == 0:
        return -1

    low = 0
    high = len(nums) - 1

    def binary_search(low, high):
        if low > high:
            return -1

        mid = low + (high - low) // 2

        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            else:
                return binary_search(mid + 1, high)

        if nums[mid] > target or nums[mid] < nums[low]:
            return binary_search(low, mid - 1)

        elif nums[mid] < target or nums[mid] > nums[high]:
            return binary_search(mid + 1, high)

        else:
            return binary_search(mid + 1, high)

    return binary_search(low, high)