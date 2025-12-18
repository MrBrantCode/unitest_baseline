"""
QUESTION:
Write a function `permute_unique(nums)` that returns all distinct permutations of a given list of integers `nums`. The function should handle duplicate elements in the list and return all distinct permutations without duplicates.
"""

def permute_unique(nums):
    nums.sort()
    result = []
    
    def permute(index, permutation):
        if index == len(nums):
            result.append(permutation[:])
            return
        
        for i in range(index, len(nums)):
            if index != i and nums[index] == nums[i]:
                continue
                
            nums[index], nums[i] = nums[i], nums[index]
            permute(index + 1, permutation + [nums[index]])
            nums[index], nums[i] = nums[i], nums[index]
    
    permute(0, [])
    return result