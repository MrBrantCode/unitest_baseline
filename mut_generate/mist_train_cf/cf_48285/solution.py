"""
QUESTION:
Write a function `minSubArrayLen` that takes two parameters: a positive integer `target` and an array of positive integers `nums`. The function should return the smallest length of a contiguous subarray in `nums` whose sum is equal to or greater than `target`. If no such subarray exists, return `0`. The function should be able to handle `1 <= target <= 10^9`, `1 <= nums.length <= 10^5`, and `1 <= nums[i] <= 10^5`.
"""

def minSubArrayLen(target, nums):
    n = len(nums)
    min_length = float('inf')  
    left = 0
    current_sum = 0
    
    for right in range(n):
        current_sum += nums[right]  
        while current_sum >= target:  
            min_length = min(min_length, right - left + 1)  
            current_sum -= nums[left]  
            left += 1  
    if min_length == float('inf'):  
        return 0
    else:
        return min_length