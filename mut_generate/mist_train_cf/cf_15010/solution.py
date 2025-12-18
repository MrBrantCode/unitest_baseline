"""
QUESTION:
Implement a function `hasSubsetSum(nums, target)` that takes a list `nums` and a target integer `target` as inputs, and returns `True` if there is a subset of `nums` that sums up to `target`, and `False` otherwise. The function should have a time complexity of O(2^n) and a space complexity of O(n).
"""

def hasSubsetSum(nums, target):
    def backtrack(nums, target, index, currentSum):
        if currentSum == target:
            return True
        if index == len(nums):
            return False

        include = backtrack(nums, target, index + 1, currentSum + nums[index])
        exclude = backtrack(nums, target, index + 1, currentSum)

        return include or exclude

    return backtrack(nums, target, 0, 0)