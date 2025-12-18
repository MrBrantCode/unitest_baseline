"""
QUESTION:
Write a function `combination_sum` that takes a list of integers `nums` and an integer `target` as input. The function should return all unique combinations of elements from `nums` such that the sum of the combination is equal to `target` and the combination contains at least 2 elements. The function should not contain duplicate combinations and each combination should not contain duplicate elements. The input list `nums` can contain duplicate elements.
"""

def combination_sum(nums, target):
    def backtrack(start, curr_combination, curr_sum):
        if curr_sum == target and len(curr_combination) >= 2:
            result.append(curr_combination[:])
            return
        if curr_sum > target:
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue
            curr_combination.append(nums[i])
            backtrack(i + 1, curr_combination, curr_sum + nums[i])
            curr_combination.pop()
    
    result = []
    nums.sort()  # Sort the input list to handle duplicates
    backtrack(0, [], 0)
    return result