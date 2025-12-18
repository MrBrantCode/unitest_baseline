"""
QUESTION:
Implement a function `maxAscendingSum(nums)` that takes an array of positive integers `nums` as input and returns the maximum possible sum of an ascending subarray in `nums`. An ascending subarray is a contiguous sequence of numbers where each element is greater than the previous one and contains no duplicates. If there are multiple subarrays with the same maximum sum, return the sum of the one with the smallest length. If there is still a tie, return the sum of the one that appears first. The input array `nums` has a length between 1 and 1000, and each element is an integer between 1 and 1000.
"""

def maxAscendingSum(nums):
    maxSum = curSum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            curSum += nums[i]
        else:
            curSum = nums[i]
        maxSum = max(maxSum, curSum)
    return maxSum