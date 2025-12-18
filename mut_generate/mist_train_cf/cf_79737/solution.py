"""
QUESTION:
Given an array of integers, write a function maxSubArray(nums) that returns the maximum possible sum of a subarray. The function should be able to handle arrays with both positive and negative integers.
"""

def maxSubArray(nums):
    """This function returns the maximum possible sum of a subarray"""
    current_sum = nums[0]
    global_sum = nums[0]

    for num in nums[1:]:
       # Take the maximum of the current number and current sum + current number
        current_sum = max(current_sum + num, num)

        # update the maximum sum
        global_sum = max(global_sum, current_sum)

    return global_sum