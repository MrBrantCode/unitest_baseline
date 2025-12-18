"""
QUESTION:
Design a function `max_subarray` that takes an array of integers and an integer `k` as input and returns the maximum subarray with at least `k` elements. The function should have a time complexity of O(n^2) and a space complexity of O(n), where n is the size of the input array.
"""

def max_subarray(nums, k):
    max_sum = float('-inf')
    start = end = -1
    prefix_sum = [0] * (len(nums) + 1)
    prefix_sum[0] = 0
    
    for i in range(len(nums)):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    for i in range(len(nums) - k + 1):
        for j in range(i + k, len(nums) + 1):
            subarray_sum = prefix_sum[j] - prefix_sum[i]
            if subarray_sum > max_sum:
                max_sum = subarray_sum
                start = i
                end = j - 1
                
    return nums[start:end+1]