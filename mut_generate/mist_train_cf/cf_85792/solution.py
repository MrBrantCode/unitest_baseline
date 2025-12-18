"""
QUESTION:
Write a function `maxSubArray(nums)` that finds the maximum contiguous subarray sum within the given array `nums` and returns the sum along with the start and end indices of the subarray. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def maxSubArray(nums):
    max_current = max_global = nums[0]
    start = end = 0
    s = 0

    for i in range(1,len(nums)):
        
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            s = i
        
        else:
            max_current = max_current + nums[i]
        
        if max_current > max_global:
            max_global = max_current
            start = s
            end = i
            
    return max_global, start, end