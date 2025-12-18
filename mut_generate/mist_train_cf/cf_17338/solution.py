"""
QUESTION:
Write a function `threeSum(nums, target)` that takes a list of positive integers `nums` and a target integer `target` as input, and returns a list of unique triplets from `nums` whose sum equals `target`. The sum of the first two elements in each triplet must be less than or equal to the third element, and the function should ignore duplicate triplets. The input list can contain duplicate integers.
"""

def threeSum(nums, target):
    nums.sort()
    triplets = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            
            if curr_sum == target:
                triplets.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    
    return triplets