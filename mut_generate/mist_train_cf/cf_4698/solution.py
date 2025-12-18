"""
QUESTION:
Write a function `combinationSum(nums, target, max_items)` that takes a list of distinct positive integers `nums`, a target number `target`, and a maximum number of items `max_items`. The function should return all unique combinations of `nums` that sum up to `target`, with each combination having at most `max_items` numbers. If no combination is found, return an empty list.
"""

def combinationSum(nums, target, max_items):
    def backtrack(start, current_combination, current_target):
        if current_target == 0:
            combinations.append(current_combination[:])
            return
        if current_target < 0:
            return
        if len(current_combination) == max_items:
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            current_combination.append(nums[i])
            backtrack(i+1, current_combination, current_target - nums[i])
            current_combination.pop()

    nums.sort()
    combinations = []
    backtrack(0, [], target)
    return combinations