"""
QUESTION:
Write a function `numberOfSubarrays(nums, k)` that takes an array of integers `nums` and an integer `k` as input, and returns the number of continuous subarrays that meet the following conditions: the subarray contains `k` odd numbers, the sum of the elements in the subarray is divisible by `k`, and the length of the subarray is less than or equal to `2k`. The input array `nums` has a length between 1 and 50,000, and each element in `nums` is between 1 and 10^5. The integer `k` is between 1 and the length of `nums`.
"""

def numberOfSubarrays(nums, k):
    prefix_sum = [0] * (len(nums) + 1)
    odd_numbers = [0] * len(nums)
    
    for i in range(len(nums)):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]
        if nums[i] % 2 == 1:
            odd_numbers[i] = 1
            
    prefix_odd = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix_odd[i+1] = prefix_odd[i] + odd_numbers[i]
        
    count = 0
    for i in range(k-1, len(nums)):
        if prefix_odd[i+1]-prefix_odd[i-k+1] == k and (prefix_sum[i+1]-prefix_sum[i-k+1]) % k == 0:
            count += 1
            
    return count