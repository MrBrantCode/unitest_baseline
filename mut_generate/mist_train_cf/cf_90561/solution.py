"""
QUESTION:
Write a function `findSubsetSum(nums, target)` that determines if a list of integers `nums` contains a subset that sums up to the target `target`. The list may contain duplicate numbers and the target sum can be negative or zero. The function should return a boolean value indicating whether such a subset exists. The time complexity should be O(2^n) and the space complexity should be O(n).
"""

def findSubsetSum(nums, target):
    def backtrack(index, current_sum):
        if current_sum == target:
            return True
        if index >= len(nums):
            return False

        if backtrack(index + 1, current_sum + nums[index]):
            return True
        if backtrack(index + 1, current_sum):
            return True

        return False

    return backtrack(0, 0)