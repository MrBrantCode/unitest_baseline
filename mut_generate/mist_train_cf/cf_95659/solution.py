"""
QUESTION:
Find all unique combinations of at least 2 elements from a given list of integers that sum up to a given target value, with no duplicate elements in each combination. 

Implement a function `find_combinations(nums, target)` where `nums` is a list of integers and `target` is the target sum.
"""

def find_combinations(nums, target):
    results = []
    combination = []
    nums.sort()  # Sort the list to ensure non-decreasing order
    
    def backtrack(start, current_sum):
        if current_sum == target and len(combination) > 1:
            results.append(combination[:])  # Append a copy of the combination
            return
        elif current_sum > target or start >= len(nums):
            return
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue  # Skip duplicates to avoid duplicate combinations
            
            combination.append(nums[i])
            backtrack(i + 1, current_sum + nums[i])
            combination.pop()
    
    backtrack(0, 0)
    return results