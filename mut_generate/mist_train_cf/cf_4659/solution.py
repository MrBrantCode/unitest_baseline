"""
QUESTION:
Find all unique combinations of at least 3 elements from a sorted list of integers that sum up to a given target value. Each combination should not contain any duplicate elements and should be in ascending order.

Function: find_combinations(nums, target, combination)
Input: 
- nums: a sorted list of integers
- target: the target sum value
- combination: the current combination of integers
Restriction: 
- The list should not contain any duplicate elements.
- The combination should be in ascending order.
- The function should return all combinations with a length of at least 3.
"""

def entrance(nums, target):
    def find_combinations(nums, target, combination):
        if target == 0 and len(combination) >= 3:
            result.append(combination)
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                break
            find_combinations(nums[i+1:], target-nums[i], combination + [nums[i]])

    nums.sort()
    result = []
    find_combinations(nums, target, [])
    return result