"""
QUESTION:
Find the longest continuous increasing subarray within the given array of integers. If multiple subarrays have the same length, return the one with the smallest starting index. Implement the solution using recursion instead of iteration. The function should take an array of integers as input and return the longest continuous increasing subarray.
"""

def longest_increasing_subarray(nums):
    def helper(i, length):
        if i == len(nums) - 1:
            return i, length
        if nums[i] < nums[i + 1]:
            return helper(i + 1, length + 1)
        return i, length

    max_length = 0
    start_index = 0
    for i in range(len(nums)):
        index, length = helper(i, 1)
        if length > max_length:
            max_length = length
            start_index = i
    return nums[start_index:start_index + max_length]