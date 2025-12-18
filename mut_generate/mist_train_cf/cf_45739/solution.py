"""
QUESTION:
Given a function `twoSumLessThanK(nums, k)`, return the maximum even sum of two numbers in the array `nums` that is less than `k`. If no such sum exists, return `-1`. The input array `nums` consists of integers and has a length between 1 and 100. Each element in `nums` is between 1 and 1000, and `k` is between 1 and 2000.
"""

def twoSumLessThanK(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    result = -1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum < k and curr_sum % 2 == 0:
            result = max(result, curr_sum)
            left += 1
        else:
            right -= 1
    return result