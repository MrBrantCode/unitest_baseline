"""
QUESTION:
Write a function named `permute_unique(nums)` that generates all distinct permutations of the given list of integers `nums` and returns them without duplicates. The function should handle duplicate elements in the input list.
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