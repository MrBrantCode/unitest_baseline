"""
QUESTION:
Write a function named `threeSum` that takes a list of integers `nums` and an integer `target` as input. The function should return a list of unique triplets from `nums` whose sum is equal to `target`. Each triplet should be represented as a list of three integers. The input list may contain duplicates, but the function should only return unique triplets. The function should have a time complexity of O(n^2), where n is the length of `nums`.
"""

def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            
            if curr_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
                    
            elif curr_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result