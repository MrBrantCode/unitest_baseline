"""
QUESTION:
Write a function named `findSubsetSum` that takes two parameters: a list of integers `nums` and an integer `target`. The function should determine if the list contains a subset that sums up to the target, including subsets with negative numbers, and handle cases where the target sum is negative or zero. The function should return a boolean value indicating whether such a subset exists. The time complexity of the solution should be O(2^n) and the space complexity should be O(n).
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