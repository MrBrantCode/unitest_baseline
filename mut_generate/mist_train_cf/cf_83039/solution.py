"""
QUESTION:
Given a sorted array `nums` and a number `target`, write a function `majority_element(nums, target)` that returns a tuple `(start_index, end_index, is_majority)` where `start_index` and `end_index` are the starting and ending indices of the `target` in the array, and `is_majority` is `True` if and only if `target` is a majority element. A majority element is an element that appears more than `N/2` times in an array of length `N`. If `target` is not found in the array, return `(-1, -1, False)`.

Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 10^9`, `1 <= target <= 10^9`.
"""

def majority_element(nums, target):
    count = nums.count(target)
    if count > len(nums) / 2:
        return (nums.index(target), len(nums) - 1 - nums[::-1].index(target), True)
    else:
        return (nums.index(target), len(nums) - 1 - nums[::-1].index(target), False) if target in nums else (-1, -1, False)