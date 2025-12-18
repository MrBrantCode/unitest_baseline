"""
QUESTION:
Write a function `threeSum` that takes an array of integers `nums` and a target value `target`, and returns a list of three indices that add up to the target. The time complexity should be O(n^2), where n is the length of the input array. Assume that the input array will always have at least three elements, and the target value will always have a unique set of three indices. The indices are 0-based, and the array may contain duplicate values.
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