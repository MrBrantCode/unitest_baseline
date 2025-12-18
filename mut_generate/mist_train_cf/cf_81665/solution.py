"""
QUESTION:
Given an unsorted integer array `nums`, write a function named `firstMissingPositive` to find the smallest missing positive integer. The array may contain duplicate values and has a length between 0 and 300, with each integer in the range `-2^31 <= nums[i] <= 2^31 - 1`. Implement an algorithm that runs in O(n) time and uses constant extra space.
"""

def firstMissingPositive(nums):
    if len(nums) == 0:
        return 1

    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            temp = nums[i] - 1
            nums[i], nums[temp] = nums[temp], nums[i]
            
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1