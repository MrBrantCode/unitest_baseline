"""
QUESTION:
Given an array of integers, write a function named threeSum that finds all unique triplets in the array that sum to zero. The function should return a list of these triplets, and each triplet should be a list of three integers. The input array may contain duplicate numbers, but the output should not contain duplicate triplets. The function should also not use the same element more than once in each triplet.
"""

def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return result