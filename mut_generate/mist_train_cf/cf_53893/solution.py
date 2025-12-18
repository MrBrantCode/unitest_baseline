"""
QUESTION:
Write a function `maxAscendingSum` that takes a list of positive integers `nums` as input and returns a tuple containing the maximum possible sum of an ascending subarray in `nums` and its corresponding start and end indices. An ascending subarray is defined as a contiguous sequence of numbers where each number is greater than the previous one. The function should have a time complexity of O(n), where n is the length of the input list. The length of the input list is guaranteed to be between 1 and 10^5, and each element in the list is a positive integer between 1 and 10^9.
"""

def maxAscendingSum(nums):
    curr_sum, max_sum = nums[0], nums[0]
    start, end, max_start, max_end = 0, 0, 0, 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            curr_sum += nums[i]
            end = i
        else:
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_start = start
                max_end = end
            curr_sum = nums[i]
            start = end = i
    if curr_sum > max_sum:    # Check for last ascending subarray
        max_sum = curr_sum
        max_start = start
        max_end = end
    return max_sum, max_start, max_end