"""
QUESTION:
Write a function `fourSum(nums, target)` that takes an array `nums` of n integers and an integer `target` as input, and returns all unique quadruplets in the array which gives the sum of `target`. The quadruplets should be returned in a sorted order (ascending order based on the first element of the quadruplet, if there is a tie, sort based on the second element, and so on). The solution set must not contain duplicate quadruplets. 

Restrictions: 
- 0 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""

def fourSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  
            l, r = j + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[j] + nums[l] + nums[r]
                if total == target:
                    result.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 
                elif total < target:
                    l += 1
                else: r -= 1
    return result