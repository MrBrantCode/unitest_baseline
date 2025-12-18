"""
QUESTION:
Write a function `threeSum(nums, target)` that takes an array of integers `nums` and a target value `target` as input, and returns a list of three indices of numbers in `nums` that add up to `target`. The function should have a time complexity of O(n^2), where n is the length of `nums`. Assume that `nums` has at least three elements and a unique set of three indices that add up to `target`.
"""

def threeSum(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    for i in range(n-2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return [i, left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1