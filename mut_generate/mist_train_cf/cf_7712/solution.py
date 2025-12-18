"""
QUESTION:
Write a function `find_combinations(nums, target)` that lists all possible combinations of four distinct elements from a given array `nums`, where the sum of the elements in each combination is equal to a given target value. The array `nums` may contain duplicate elements and can include negative numbers. The target value can also be negative.
"""

def find_combinations(nums, target):
    nums.sort()
    result = []  # Initialize result list to store combinations

    def backtrack(combination, start_index, target):
        if len(combination) == 4:  
            if sum(combination) == target:
                result.append(combination[:])  # Append the combination if sum is equal to target
            return

        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i-1]:
                continue  

            combination.append(nums[i])
            backtrack(combination, i+1, target - nums[i])  
            combination.pop()  

    backtrack([], 0, target)
    return result  # Return the result list