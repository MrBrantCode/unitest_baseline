"""
QUESTION:
Given a function max_subarray_sum(arr, k), where arr is a list of integers and k is an integer, find the maximum sum of a subarray that is less than or equal to k, and return the starting and ending indices of that subarray. If there are multiple subarrays with the maximum sum, return the indices of the longest subarray among them.
"""

def max_subarray_sum(arr, k):
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    max_sum = float('-inf')
    max_length = 0
    start_index = end_index = -1
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray_sum = prefix_sum[j + 1] - prefix_sum[i]
            
            if subarray_sum > max_sum and subarray_sum <= k:
                max_sum = subarray_sum
                max_length = j - i + 1
                start_index = i
                end_index = j
            elif subarray_sum == max_sum and j - i + 1 > max_length:
                max_length = j - i + 1
                start_index = i
                end_index = j
                
    return start_index, end_index