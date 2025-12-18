"""
QUESTION:
Implement the `max_subarray_sum` function to find the maximum sum of a contiguous subarray within the given list of integers. The function should take a list of integers as input and return the maximum sum. Optimize the time complexity of the function while maintaining the same functionality.
"""

def maxSubArray(nums):
    def max_crossing_sum(nums, low, mid, high):
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, low - 1, -1):
            current_sum += nums[i]
            if current_sum > left_sum:
                left_sum = current_sum

        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, high + 1):
            current_sum += nums[i]
            if current_sum > right_sum:
                right_sum = current_sum

        return left_sum + right_sum

    def max_subarray_sum_helper(nums, low, high):
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        return max(max_subarray_sum_helper(nums, low, mid),
                   max_subarray_sum_helper(nums, mid + 1, high),
                   max_crossing_sum(nums, low, mid, high))

    return max_subarray_sum_helper(nums, 0, len(nums) - 1)