"""
QUESTION:
Write a function `max_sub_array` that takes an integer array `nums` as input and returns the maximum sum of a contiguous subarray along with the start and end indexes of the subarray. The function should handle arrays of any length, and the time complexity should be linear.
"""

def max_sub_array(nums):
    max_sum = cur_sum = nums[0]
    start = end = 0
    for i in range(1, len(nums)):
        if nums[i] > cur_sum + nums[i]:
            cur_sum = nums[i]
            start = i
        else:
            cur_sum += nums[i]

        if cur_sum > max_sum:
            max_sum = cur_sum
            end = i

    return max_sum, start, end