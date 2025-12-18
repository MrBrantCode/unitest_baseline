"""
QUESTION:
You are given an integer array `nums` representing the monetary value in each house arranged linearly. Determine the highest possible sum of money you can pilfer without triggering the police alarm, which is triggered by burgling two contiguous houses. Implement the function `rob(nums)` to return this maximum sum. The constraints are `1 <= nums.length <= 100` and `0 <= nums[i] <= 400`.
"""

def entrance(nums):
    if not nums: return 0
    if len(nums) <= 2: return max(nums)

    prev1, prev2 = 0, 0
    for num in nums:
        prev1, prev2 = prev2, max(prev1 + num, prev2)
        
    return prev2