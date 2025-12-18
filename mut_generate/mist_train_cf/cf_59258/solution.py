"""
QUESTION:
Given an unsorted array of integers `nums` where `0 <= nums.length <= 300` and `-2^31 <= nums[i] <= 2^31 - 1`, find the smallest absent positive integer. Design an algorithm that operates in `O(n)` time complexity and utilizes constant extra space.
"""

def firstMissingPositive(nums):
    if len(nums) == 0: 
        return 1 

    n = len(nums)

    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    for num in nums:
        num = abs(num)
        if num > n:
            continue
        else:
            nums[num-1] = -abs(nums[num-1])

    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1